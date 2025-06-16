# django_project
# Fitness Studio Booking API (Django)

This is a simple Booking API built using Django REST Framework for a fictional fitness studio. It allows users to view available fitness classes, book a spot, and view their bookings.

---

## Features

- View all upcoming fitness classes
- Book a class by providing your details
- Retrieve bookings using your email address
- Handles slot availability, input validation, and timezone conversions (IST by default)

---

## Tech Stack

- Python 3.x
- Django 4.x
- Django REST Framework
- SQLite (in-memory lightweight database)

---

## Setup Instructions

### 1. Clone the Repository or Unzip
If using Git:
```bash
git clone https://github.com/pooja8837/fitness-booking-api.git
cd fitness-booking-api

If using ZIP, extract and open the fitness_booking folder in your terminal.

2. Create and Activate Virtual Environment

python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Run Migrations and Seed Data
python manage.py makemigrations
python manage.py migrate
python seed_data.py

5. Run the Server
python manage.py runserver
Server will start at: http://127.0.0.1:8000/

API Endpoints
GET /classes
Returns all upcoming fitness classes.

POST /book
Books a class using class ID, name, and email.

GET /bookings?email=email@example.com
Returns all bookings made by a specific email.

Sample API Requests

🔹 GET /classes
cURL:
curl http://127.0.0.1:8000/classes/
Postman:

Method: GET
URL: http://127.0.0.1:8000/classes/

🔹 POST /book
cURL:
curl -X POST http://127.0.0.1:8000/book/ \
-H "Content-Type: application/json" \
-d '{"class_id": 1, "client_name": "Pooja", "client_email": "pooja@example.com"}'
Postman:

Method: POST
URL: http://127.0.0.1:8000/book/

Body (raw JSON):
{
  "class_id": 1,
  "client_name": "Pooja",
  "client_email": "pooja@example.com"
}

🔹 GET /bookings?email=pooja@example.com
cURL:
curl "http://127.0.0.1:8000/bookings?email=pooja@example.com"
Postman:

Method: GET
URL: http://127.0.0.1:8000/bookings?email=pooja@example.com

Timezone Handling
All class timings are stored in IST (Asia/Kolkata).

You can extend timezone conversion using Django’s timezone utilities.

Error Handling
400: Missing or invalid fields

404: Class not found

409: No slots available (overbooking)

Author
Developed by Pooja Chaudhari
Email: poojachaudhari8837@gmail.com
GitHub: github.com/pooja8837

---

This README now includes:
- Full setup steps 
- Sample cURL requests  
- Postman details 
- API endpoints with usage 
- Loom walkthrough placeholder 