import logging
import pyodbc
import os
import json
import azure.functions as func

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="http_trigger")
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing request for payment status.")

    # Retrieve the student_id parameter
    student_id = req.params.get('student_id')
    logging.info(f"Received StudentID: {student_id}")

    if not student_id:
        return func.HttpResponse("Please provide a valid StudentID", status_code=400)

    # Ensure the student_id is a string
    student_id = str(student_id)

    try:
        # Retrieve the connection string from environment variables
        conn_str = os.getenv("SQL_CONNECTION_STRING")
        if not conn_str:
            logging.error("SQL_CONNECTION_STRING is not set in environment variables.")
            return func.HttpResponse("Internal Server Error", status_code=500)

        logging.info(f"Connecting to the database using connection string: {conn_str}")

        # Connect to the SQL Server
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        # Query to fetch payment details for the given student ID
        query = "SELECT paid, total, name FROM students WHERE id = ?"
        logging.info(f"Executing query: {query} with student_id: {student_id}")
        cursor.execute(query, (student_id,))
        row = cursor.fetchone()

        if not row:
            logging.warning(f"No data found for Student ID: {student_id}")
            return func.HttpResponse("Student not found", status_code=404)

        # Retrieve payment details
        paid_amount, total_fee, name = row
        logging.info(f"Student {student_id}: Paid: {paid_amount}, Name: {name}, Total: {total_fee}")

        # Calculate the remaining fee
        remaining_amount = total_fee - paid_amount
        paid_amount = float(paid_amount)
        total_fee = float(total_fee)
        remaining_amount = float(remaining_amount)

        # Determine payment status
        if paid_amount == total_fee:
            status = "Paid"
        elif paid_amount > 0:
            status = "Partially Paid"
        else:
            status = "Overdue"

        # Construct the response with additional details
        response = {
            "StudentID": student_id,
            "Name": name,
            "Status": status,
            "TotalFee": total_fee,
            "PaidAmount": paid_amount,
            "RemainingAmount": remaining_amount
        }
        return func.HttpResponse(json.dumps(response), status_code=200, mimetype="application/json")

    except pyodbc.Error as db_error:
        logging.error(f"Database error occurred: {str(db_error)}")
        return func.HttpResponse("Database connection error", status_code=500)

    except Exception as e:
        logging.error(f"Unexpected error occurred: {str(e)}")
        return func.HttpResponse("Internal Server Error", status_code=500)
