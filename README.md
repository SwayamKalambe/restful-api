# Fashion Items API

## Overview
Fashion Items API is a RESTful API built using FastAPI for managing fashion items. It provides secure endpoints for user registration, login, and CRUD operations on fashion items, with JWT authentication and secure password hashing.

## Features
- User authentication using JWT tokens
- Secure password hashing with bcrypt
- CRUD operations for fashion items
- Input validation with Pydantic models
- Integration with PostgreSQL for data storage
- Protected endpoints with OAuth2 for user access
- User registration and login system

## Tech Stack
- FastAPI
- PostgreSQL
- SQLAlchemy ORM
- Pydantic
- Python-Jose (JWT)
- Passlib (Password Hashing)
- Python 3.x

## Prerequisites
- Python 3.x
- PostgreSQL database
- pip (Python package manager)

## Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/SwayamKalambe/restful-api.git
   cd <repository-directory>
   ```

2. **Install Required Packages:**
   ```bash
   pip install fastapi[all] sqlalchemy psycopg2-binary python-jose[cryptography] passlib[bcrypt]
   ```

3. **Configure the Database:**
   - Create a PostgreSQL database.
   - Update the `DATABASE` URL in `database.py`:
     ```python
     import os
     DATABASE = os.getenv("DATABASE_URL")
     ```
   
4. **Generate and Configure the Secret Key:**
   - The secret key used for JWT authentication should be securely generated and stored in an environment variable.
   - To generate a secret key:
     ```python
     import secrets
     print(secrets.token_hex(32))
     ```
     This will generate a secure 64-character hexadecimal string.
   
   - Store the secret key in the `.env` file:
     ```bash
     SECRET_KEY="your_generated_secret_key_here"
     ```

5. **Create Database Tables:**
   - Run the following command to initialize the database:
     ```bash
     python create_table.py
     ```

6. **Start the Application:**
   - Run the server locally:
     ```bash
     uvicorn main:app --reload
     ```
   - The application will be available at `http://localhost:8000`.

## Project Structure
- `main.py`: Main application and API routes.
- `models.py`: SQLAlchemy models for database tables.
- `schema.py`: Pydantic models for request and response validation.
- `database.py`: Database configuration and session management.
- `auth.py`: Authentication logic including JWT handling.
- `create_table.py`: Script for initializing the database tables.

## API Endpoints

### Authentication Endpoints
- **POST /register**  
  Registers a new user with a unique username and email.
  
- **POST /token**  
  Authenticates a user and provides a JWT token for accessing protected endpoints.

### Fashion Items Endpoints (Protected)
All fashion item-related endpoints require authentication via a Bearer token.

- **GET /items**  
  Retrieves a list of all fashion items in the store.
  
- **POST /items**  
  Adds a new fashion item to the store.

- **GET /items/{item_id}**  
  Retrieves details of a specific fashion item by its ID.

- **PUT /items/{item_id}**  
  Updates an existing fashion item.

- **PATCH /items/{item_id}**  
  Partially updates specific fields of a fashion item.

- **DELETE /items/{item_id}**  
  Deletes a fashion item by its ID.

## Data Models

- **Fashion Item:**  
  Contains attributes such as `id`, `name`, `price`, and `description`.

- **User:**  
  Contains `username`, `email`, and `password` (hashed for security).

## Security
- **Password Hashing:**  
  Passwords are securely hashed using bcrypt before being stored in the database.

- **JWT Authentication:**  
  JWT tokens are used to authenticate users, with tokens expiring after 30 minutes.

- **Protected Routes:**  
  Endpoints for managing fashion items require a valid JWT token for access.

- **Input Validation:**  
  Pydantic models are used for request/response validation to ensure data integrity.

## Error Handling
The API includes comprehensive error handling for:
- Invalid credentials
- Duplicate email or username during registration
- Item not found
- Invalid or expired JWT tokens
- Validation errors

## Development Notes
- **Logging and Rate Limiting:**  
  Consider implementing logging and rate limiting for production deployment to enhance security and monitor performance.
