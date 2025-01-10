1. Project Overview

This solution aims to provide a cloud-native student fee management system leveraging various Azure services. The system is designed to automate fee notifications, provide a secure API for managing and querying fee details, and allow role-based access for students and administrators. The project is built on Azure’s serverless computing, data storage, and automation features.
2. Solution Architecture

Azure SQL Database: Stores structured fee records for students and administrators.
Azure Functions: Serves as the backend to calculate fees, provide API endpoints, and handle other serverless computing requirements.
Azure Logic Apps: Automates fee reminders and other notifications for students.
Azure API Management: Securely exposes the fee-related APIs to students and administrators.
Azure AD Authentication & RBAC: Manages role-based access control for administrators.
Azure Application Insights: Monitors the entire solution and provides insights into performance and failures.


