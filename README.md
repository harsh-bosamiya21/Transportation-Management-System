# Transportation Management System (TMS)

A Django-based application designed to manage transportation operations effectively.

## Features
- **User Authentication:** Sign up, log in, and manage profiles.
- **Customer & Driver Management:** Add and manage customers and drivers.
- **Shipment Tracking:** Create shipments and track their status.
- **Email Notifications:** Automatically send emails regarding shipment updates.

## Tech Stack
- **Backend:** Python, Django
- **Database:** MySQL
- **Frontend:** HTML, CSS, JavaScript (Django Templates)

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/harsh-bosamiya21/Transportation-Management-System.git
   ```

2. **Create a virtual environment & install dependencies:**
   ```bash
   python -m venv venv
   source venv/Scripts/activate
   pip install -r requirements.txt
   ```

3. **Database Configuration:**
   - Ensure MySQL is running on port `3306`.
   - Update `DATABASES` in `tms_app/settings.py` with your MySQL credentials, testing with the db `tms_db`.
   
4. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the local development server:**
   ```bash
   python manage.py runserver
   ```
