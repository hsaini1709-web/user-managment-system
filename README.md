# Django REST Framework - User Management System

## 1. Project Description

This project is a User Management System developed using Django and Django REST Framework. It provides REST APIs to create, retrieve, update, and manage users securely.

## 2. Features

- Custom User Model using `AbstractUser`
- User Registration
- List and Retrieve Users
- Update User Details
- Soft Delete (Active/Inactive Status)
- JWT Authentication
- Email OTP Generation and Verification
- Forgot Password
- Reset Password
- Welcome Email on User Registration

## 3. Technologies Used

- Python
- Django
- Django REST Framework
- SQLite
- Simple JWT
- Pillow
- python-dotenv

## 4. Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/hsaini1709-web/user-managment-system.git
```

### Step 2: Open the Project Folder

```bash
cd user-managment-system
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

### Step 5: Install Required Packages

```bash
pip install -r requirements.txt
```

### Step 6: Configure Environment Variables

Create a `.env` file in the project root directory (the same folder as `manage.py`).

Add the following variables:

```env
SECRET_KEY=your_django_secret_key
EMAIL_HOST_USER=your_email_address
EMAIL_HOST_PASSWORD=your_email_app_password
```

Use your own configuration values. Never upload the `.env` file to GitHub.

### Step 7: Apply Database Migrations

```bash
python manage.py migrate
```

### Step 8: Start the Development Server

```bash
python manage.py runserver
```

The development server will run at:

`http://127.0.0.1:8000/`

## 5. API Endpoints

### Authentication APIs

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/api/auth/login/` | Login with email and password |
| POST | `/api/auth/send-otp/` | Send verification OTP |
| POST | `/api/auth/verify-otp/` | Verify OTP |
| POST | `/api/auth/forgot-password/` | Request password reset |
| POST | `/api/auth/reset-password/` | Reset password |

### User Management APIs

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/api/users/` | Create a user |
| GET | `/api/users/` | List all users |
| GET | `/api/users/1/` | Retrieve a user |
| PATCH | `/api/users/1/` | Update user details |
| DELETE | `/api/users/1/` | Soft delete a user |

## 6. Authentication

JWT authentication is implemented using Django REST Framework Simple JWT.

After successful login, use the returned access token to access protected User APIs.

Add this header to your requests:

```http
Authorization: Bearer YOUR_ACCESS_TOKEN
```

## 7. Sample API Requests

### Login

**POST** `/api/auth/login/`

```json
{
    "email": "user@example.com",
    "password": "your_password"
}
```

### Send OTP

**POST** `/api/auth/send-otp/`

```json
{
    "email": "user@example.com"
}
```

### Verify OTP

**POST** `/api/auth/verify-otp/`

```json
{
    "email": "user@example.com",
    "otp": "123456"
}
```

### Forgot Password

**POST** `/api/auth/forgot-password/`

```json
{
    "email": "user@example.com"
}
```

### Reset Password

**POST** `/api/auth/reset-password/`

```json
{
    "email": "user@example.com",
    "otp": "123456",
    "new_password": "NewStrongPassword123!"
}
```

*Note: These are sample values. Use a registered email address and the actual OTP received in your email when testing.*

## 8. Email Configuration

This project uses email configuration to send:

- Welcome emails after user registration.
- OTP verification emails.
- Password reset OTP emails.

Email credentials and Django SECRET_KEY are stored in environment variables using a `.env` file.

For security reasons, never upload real email credentials or secret keys to GitHub.

## 9. Database

SQLite is used as the default database.

Django migrations are used to create and update database tables.

## 10. Postman Collection

A Postman collection is included in this repository:

`Django_User_Management_System.postman_collection.json`

Import this file into Postman to test the available APIs.

## 11. Developer

Developed as an internship assignment using Django and Django REST Framework.
