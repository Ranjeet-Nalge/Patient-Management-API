Patient Management API
======================

A simple REST API for managing patient data using FastAPI and Pydantic. Supports CRUD operations and validation for all patient data.

Features
--------

- Add a new patient
- View all patients
- Get patient by ID
- Get patient by contact number
- Update patient details
- Delete patient
- Input validation using Pydantic
- Data stored in a JSON file

Installation
------------

1. Clone the repository:
   git clone <repo-url>
   cd Patient-Management-API

2. Create and activate a virtual environment:
   python -m venv env
   # Linux / macOS
   source env/bin/activate
   # Windows
   env\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

4. Run the API:
   uvicorn main:app --reload

API will be available at: http://127.0.0.1:8000

Swagger docs: http://127.0.0.1:8000/docs

Endpoints
---------

Method | Endpoint                    | Description
-------|-----------------------------|--------------------------
GET    | /                            | Homepage message
GET    | /view                        | View all patients
GET    | /patient/{patient_id}        | Get patient by ID
GET    | /phone/{patient_phone_number     | Get patient by contact number
POST   | /add                         | Add a new patient
PUT    | /update/{patient_id}         | Update patient details
DELETE | /patients/{patient_id}       | Delete a patient by ID

Patient Data Model / Validation
-------------------------------

Field       | Type   | Constraints                     | Example
------------|--------|---------------------------------|-------------------------------
patient_id  | int    | >0, required                    | 101
name        | str    | required                         | "Jon Doe"
age         | int    | 1–120, required                  | 30
weight      | float  | required                         | 60.5
symptoms    | list   | 1–5 items, required              | ["fever", "cough"]
contact     | dict   | max 3 keys: phone, email, address| {"phone": "+91-9876543210", "address": "123 MG Road"}

Usage
-----

- Use Postman or Swagger docs to test endpoints.
- Add patient data as JSON in POST requests.
- Update only the fields you want; existing fields remain unchanged.

Notes
-----

- Data persists in patient_data_json.json.
- No database required, everything is stored in JSON.
- API is designed to be simple but extensible for more features.

Author
------
Ranjeet Nalge
