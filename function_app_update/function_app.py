import logging
import pyodbc
import json
import azure.functions as func
import os

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="update_fee", methods=["PUT"])
def update_fee(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing PUT request for fee status update.")

    try:
        # Parse the request body
        req_body = req.get_json()
        student_id = req_body.get('student_id')
        additional_paid = req_body.get('amount_paid')

        # Validate input
        if student_id is None or additional_paid is None:
            return func.HttpResponse(
                json.dumps({"error": "Missing required fields: student_id, amount_paid"}),
                status_code=400,
                mimetype="application/json"
            )

        if not isinstance(student_id, (str, int)) or not isinstance(additional_paid, (int, float)):
            return func.HttpResponse(
                json.dumps({"error": "Invalid input types. 'student_id' must be a string or integer, 'amount_paid' must be a number."}),
                status_code=400,
                mimetype="application/json"
            )

    except ValueError as e:
        logging.error(f"Error parsing JSON: {e}")
        return func.HttpResponse(
            json.dumps({"error": "Invalid JSON data"}),
            status_code=400,
            mimetype="application/json"
        )

    # Database connection
    conn_str = os.getenv("SQL_CONNECTION_STRING")

    try:
        with pyodbc.connect(conn_str) as conn:
            cursor = conn.cursor()

            # Fetch current fee details
            query = "SELECT total, paid FROM students WHERE id = ?"
            cursor.execute(query, (str(student_id),))
            result = cursor.fetchone()

            if not result:
                return func.HttpResponse(
                    json.dumps({"error": "Student not found."}),
                    status_code=404,
                    mimetype="application/json"
                )

            # Convert Decimal to float
            total_fee = float(result[0])  # Total fee
            current_paid = float(result[1])  # Current paid amount

            # Update the `paid` amount
            updated_paid = current_paid + float(additional_paid)

            # Determine the new status
            new_status = "Complete" if updated_paid >= total_fee else "Pending"

            # Update the database
            update_query = """
                UPDATE students
                SET paid = ?, status = ?
                WHERE id = ?
            """
            cursor.execute(update_query, (updated_paid, new_status, str(student_id)))
            conn.commit()

        # Return response
        return func.HttpResponse(
            json.dumps({
                "message": "Fee record updated successfully",
                "student_id": student_id,
                "paid": updated_paid,
                "status": new_status
            }),
            status_code=200,
            mimetype="application/json"
        )

    except Exception as e:
        logging.error(f"Database error: {e}")
        return func.HttpResponse(
            json.dumps({"error": "Internal server error"}),
            status_code=500,
            mimetype="application/json"
        )
