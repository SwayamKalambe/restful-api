# Fashion Items API

A RESTful API built with FastAPI for managing fashion items with JWT authentication. The API provides secure endpoints for creating, reading, updating, and deleting fashion items, along with user registration and authentication.

---

## Features

- User authentication with JWT tokens
- Secure password hashing using bcrypt
- CRUD operations for fashion items
- Input validation using Pydantic models
- PostgreSQL database integration
- Protected endpoints with OAuth2
- User registration and login system

---

## Tech Stack

- **FastAPI**
- **PostgreSQL**
- **SQLAlchemy ORM**
- **Pydantic**
- **Python-Jose (JWT)**
- **Passlib (Password Hashing)**
- **Python 3.x**

---

## Prerequisites

- Python 3.x
- PostgreSQL
- pip (Python package manager)

---

## Installation

### 1. Clone the repository
```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Install required packages
```bash
pip install fastapi[all] sqlalchemy psycopg2-binary python-jose[cryptography] passlib[bcrypt]
```

### 3. Configure the database
- Create a PostgreSQL database.
- Update the database URL in `database.py`:
  ```python
  DATABASE = "postgresql://username:password@localhost/fashion_db"
  ```

### 4. Create database tables
Run the following command to initialize the database:
```bash
python create_table.py
```

### 5. Start the application
Run the server locally:
```bash
uvicorn main:app --reload
```

The application will be available at `http://localhost:8000`.

---

## Project Structure

```
├── main.py           # Main application and API routes
├── models.py         # SQLAlchemy models
├── schema.py         # Pydantic models for request/response
├── database.py       # Database configuration
├── auth.py           # Authentication logic
└── create_table.py   # Database initialization
```

---

## API Endpoints

### Authentication Endpoints

#### **Register User**
Registers a new user with a unique username and email.

**Request**:
```http
POST /register
Content-Type: application/json

{
  "username": "string",
  "email": "user@example.com",
  "password": "string"
}
```
**Response**:
```json
{
  "id": 1,
  "username": "string",
  "email": "user@example.com"
}
```

#### **Login**
Authenticates a user and provides a JWT token.

**Request**:
```http
POST /token
Content-Type: application/x-www-form-urlencoded

username=<username>&password=<password>
```
**Response**:
```json
{
  "access_token": "<token>",
  "token_type": "bearer"
}
```

---

### Fashion Items Endpoints

All fashion item endpoints require authentication (Bearer token).

#### **Get All Items**
Retrieves a list of fashion items.

**Request**:
```http
GET /items
Authorization: Bearer <token>
```
**Response**:
```json
[
  {
    "id": 1,
    "name": "Summer Dress",
    "price": 49.99,
    "description": "Beautiful summer dress"
  },
  {
    "id": 2,
    "name": "Winter Coat",
    "price": 99.99,
    "description": "Warm and stylish winter coat"
  }
]
```

#### **Create Item**
Adds a new fashion item.

**Request**:
```http
POST /items
Authorization: Bearer <token>
Content-Type: application/json

{
  "name": "string",
  "price": float,
  "description": "string"
}
```
**Response**:
```json
{
  "id": 3,
  "name": "string",
  "price": float,
  "description": "string"
}
```

#### **Get Item by ID**
Retrieves a specific fashion item by ID.

**Request**:
```http
GET /items/{item_id}
Authorization: Bearer <token>
```
**Response**:
```json
{
  "id": 1,
  "name": "Summer Dress",
  "price": 49.99,
  "description": "Beautiful summer dress"
}
```

#### **Update Item**
Updates an existing fashion item.

**Request**:
```http
PUT /items/{item_id}
Authorization: Bearer <token>
Content-Type: application/json

{
  "name": "string",
  "price": float,
  "description": "string"
}
```
**Response**:
```json
{
  "id": 1,
  "name": "string",
  "price": float,
  "description": "string"
}
```

#### **Partial Update Item**
Updates specific fields of a fashion item.

**Request**:
```http
PATCH /items/{item_id}
Authorization: Bearer <token>
Content-Type: application/json

{
  "name": "string",
  "price": float
}
```
**Response**:
```json
{
  "id": 1,
  "name": "string",
  "price": float,
  "description": "Beautiful summer dress"
}
```

#### **Delete Item**
Deletes a fashion item by ID.

**Request**:
```http
DELETE /items/{item_id}
Authorization: Bearer <token>
```
**Response**:
```json
{
  "detail": "Item deleted successfully"
}
```

---

## Data Models

### Fashion Item
```json
{
  "id": int,
  "name": string,
  "price": float,
  "description": string
}
```

### User
```json
{
  "username": string,
  "email": string,
  "password": string  # Stored as hashed value
}
```

---

## Security

- Passwords are hashed using bcrypt.
- JWT tokens expire after 30 minutes.
- Protected routes require a valid JWT token.
- Email and username uniqueness validation.
- Input validation using Pydantic models.

---

## Error Handling

The API implements proper error handling for:
- Invalid credentials
- Duplicate email/username
- Item not found
- Invalid token
- Validation errors

Example Error Response:
```json
{
  "detail": "Invalid credentials"
}
```

---

## Development Notes

- The secret key in `auth.py` should be moved to environment variables in production.
- Database URL should be configured via environment variables.
- Implement proper logging for production use.
- Consider adding rate limiting for production deployment.

