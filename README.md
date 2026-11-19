# Django REST Framework - User Management System

## 1. Project Description

This project is a User Management System developed using Django and Django REST Framework. It provides APIs to create, view, update, and manage users.

## 2. Features

- Custom User Model using AbstractUser
- User Registration
- List all users
- Retrieve user details
- Update user details
- Soft Delete (Active/Inactive status)
- JWT Authentication
- OTP Generation and Verification
- Forgot Password
- Reset Password
- Welcome Email on User Registration

## 3. Technologies Used

- Python
- Django
- Django REST Framework
- SQLite Database
- Simple JWT
- Pillow

## 4. Installation

Clone or download the project.

Install the required packages:

```bash
pip install -r requirements.txt
```

Run database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Open the project:

`http://127.0.0.1:8000/`

## 5. API Endpoints

Method	Endpoint	Purpose
POST	/api/users/	Create user
GET	/api/users/	List users
GET	/api/users/1/	Get user details
PATCH	/api/users/1/	Update user
DELETE	/api/users/1/	Soft delete user
POST	/api/auth/login/	Email login with JWT
POST	/api/auth/send-otp/	Send OTP
POST	/api/auth/verify-otp/	Verify OTP
POST	/api/auth/forgot-password/	Forgot password
POST	/api/auth/reset-password/	Reset password
## Setup Instructions

1. Clone or download this project.

2. Open the project folder in VS Code.

3. Create a virtual environment:

   python -m venv venv

4. Activate the virtual environment:

   venv\Scripts\activate

5. Install required packages:

   pip install -r requirements.txt

6. Apply database migrations:

   python manage.py migrate

7. Start the development server:

   python manage.py runserver

8. Open the project in your browser:

   http://127.0.0.1:8000/

## 6. Authentication

JWT authentication is implemented using Django REST Framework Simple JWT.

## 7. Database

SQLite is used as the database.

## 8. Developer

Developed as an internship assignment using Django REST Framework.
## Email Configuration

This project uses SMTP email configuration for sending welcome emails and OTP verification codes.

Email credentials and Django SECRET_KEY are stored in a `.env` file.

Create a `.env` file in the project root and configure:

- SECRET_KEY
- EMAIL_HOST_USER
- EMAIL_HOST_PASSWORD

Never upload the `.env` file to GitHub.