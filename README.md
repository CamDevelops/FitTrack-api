# FitTrack API

A RESTful API built with Python and Flask for user account management. This is the backend foundation for a full calorie and fitness tracking application.

## About

FitTrack API handles user authentication and account management. It is designed to eventually support calorie logging, goal tracking, and AI-powered nutrition insights.

## Tech Stack

- Python
- Flask
- JSON

## Getting Started

### Prerequisites

Make sure you have Python and Flask installed:

```bash
pip install flask
```

### Running the API

```bash
python app.py
```

The server will start at `http://127.0.0.1:5000`

## API Endpoints

### POST /signup

Creates a new user account.

**Required fields:**

| Field | Type | Description |
|---|---|---|
| name | string | User's full name |
| username | string | Unique username |
| email | string | User's email address |
| password | string | Account password |
| number | string | Phone number |
| age | integer | User's age |

**Example request:**

```json
{
    "name": "John Doe",
    "username": "johndoe",
    "email": "john@example.com",
    "password": "securepassword",
    "number": "555-1234",
    "age": 25
}
```

**Success response:**

Returns the updated list of users with status 200.

**Error response:**

If any required fields are missing:

```json
{
    "error": "['email', 'password'] missing"
}
```

## Planned Features

- User login with authentication
- Password hashing for security
- Input validation (email format, age as integer, password rules)
- Persistent database storage
- Calorie logging endpoints
- Goal weight and height tracking
- AI-powered calorie calculation

## Project Status

🚧 In active development