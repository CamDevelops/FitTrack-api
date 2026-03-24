# Shredly-Auth 💪

> A RESTful authentication API for a fitness tracking application — built with Python and Flask.

This project is a **backend-focused portfolio piece** demonstrating real-world API design, secure authentication, and clean project architecture. The backend was hand-coded by me using my own knowledge, research, and references like Stack Overflow and the official docs — no AI generation. The frontend (landing/login/signup pages) is largely AI-assisted and exists mainly to demo the API visually.

---

## What It Does

Shredly-Auth handles the full user authentication lifecycle for a fitness app:

- **Register** a new account with validated input
- **Login** and receive a JWT access token
- **Reset your password** via a secure token-based flow
- **Access protected routes** using JWT authorization headers

The fitness-tracking features (dashboard, calorie logging, workout plans, progress charts) are planned next iterations — the auth layer is the current focus.

---

## Tech Stack

### Backend
| Tool | Purpose |
|---|---|
| Python + Flask | Core framework |
| Flask-SQLAlchemy | ORM / database management |
| SQLite | Persistent storage |
| bcrypt | Password hashing with salt |
| Flask-JWT-Extended | JWT token issuance and validation |
| Flask-CORS | Cross-origin request handling |
| python-dotenv | Environment variable management |

### Frontend *(AI-assisted)*
| Tool | Purpose |
|---|---|
| HTML5 / CSS3 | Structure and styling |
| Vanilla JavaScript | Client-side interactivity |
| Canvas API | Animated particle background |

---

## Project Structure

```
Shredly-Auth/
├── database/
│   ├── __init__.py
│   ├── db.py              # Database initialization
│   └── models.py          # User model
├── routes/
│   ├── __init__.py
│   └── auth.py            # Auth routes (register, login, reset)
├── static/
│   ├── index.html         # Landing page
│   └── src/
│       ├── js/
│       │   ├── app.js
│       │   └── background.js
│       └── styles/
│           └── main.css
├── instance/
│   └── database.db
├── .env                   # JWT secret (not committed)
├── app.py                 # Entry point
├── config.py              # App configuration
└── requirements.txt
```

---

## API Reference

### `POST /signup`

Creates a new user account with full input validation.

**Request body:**
```json
{
  "name": "Alex Johnson",
  "username": "alexj99",
  "email": "alex@example.com",
  "password": "MySecure@Pass123",
  "ph_number": "555-1234",
  "age": 25
}
```

**Validation rules:**
- `email` — must contain `@` and `.`
- `password` — min 12 characters, at least one special character (`!@#$%^&*`), no spaces
- `age` — must be an integer
- `email` and `username` — must be unique

**Responses:**

| Status | Body |
|---|---|
| 201 | `{ "message": "Account has been Created!" }` |
| 400 | `{ "error": "['email'] missing" }` |
| 400 | `{ "error": "Please Enter a valid email." }` |
| 400 | `{ "error": "Password must be at least 12 characters long." }` |
| 400 | `{ "error": "Password must contain a special Character !@#$%^&*" }` |
| 409 | `{ "error": "That email is already registered." }` |
| 409 | `{ "error": "That username has been taken." }` |

---

### `POST /login`

Authenticates a user and returns a JWT.

**Request body:**
```json
{
  "email": "alex@example.com",
  "password": "MySecure@Pass123"
}
```

**Responses:**

| Status | Body |
|---|---|
| 200 | `{ "message": "You have been logged in!", "access_token": "<jwt>" }` |
| 400 | `{ "error": "Please enter a valid email address." }` |
| 401 | `{ "error": "Your password is incorrect!!" }` |

---

### `POST /reset-password`

Initiates or completes a password reset flow using a secure token.

> Token-based reset — no plaintext passwords transmitted.

---

### `GET /protected`

A sample protected route requiring a valid JWT.

**Headers:**
```
Authorization: Bearer <your-jwt-token>
```

**Responses:**

| Status | Body |
|---|---|
| 200 | `{ "message": "Access granted to protected route!" }` |
| 401 | `{ "msg": "Missing Authorization Header" }` |

---

## Getting Started

### Prerequisites
- Python 3.7+
- pip

### Setup

```bash
# Clone the repo
git clone <your-repo-url>
cd Shredly-Auth

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env with your JWT secret
echo "JWT_SECRET_KEY=your-secret-key-here" > .env

# Start the server
python app.py
```

App runs at `http://127.0.0.1:5000`

---

## Testing the API

```bash
# Register
curl -X POST http://127.0.0.1:5000/signup \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test User",
    "username": "testuser",
    "email": "test@example.com",
    "password": "SecurePass@123",
    "ph_number": "555-0000",
    "age": 25
  }'

# Login
curl -X POST http://127.0.0.1:5000/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "SecurePass@123"
  }'

# Access protected route
curl -X GET http://127.0.0.1:5000/protected \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

---

## Security Practices

- Passwords hashed with **bcrypt** + salt — never stored in plaintext
- **JWT tokens** for stateless, expirable session management
- **SQLAlchemy ORM** prevents SQL injection
- **Unique DB constraints** on email and username
- Secrets managed via **environment variables**, never hardcoded
- Error messages are user-facing only — no stack traces or internals exposed
- CORS configured explicitly

---

## Implementation Notes

**Backend** — all code written manually. Built by working through Flask/SQLAlchemy docs, Stack Overflow, and trial and error — with AI used for guidance and debugging discussion, not code generation.

**Frontend** — largely AI-assisted. It exists to give the API a visual interface but isn't the focus of this project.

---

## Roadmap

- [x] User registration with validation
- [x] JWT login / authentication
- [x] Password reset flow
- [x] Protected route middleware
- [ ] User profile endpoint
- [ ] Dashboard
- [ ] Calorie logging
- [ ] Goal tracking
- [ ] Progress charts
- [ ] Workout plans

---

## License

MIT — free to use for learning and reference.

---

*Built by Cameron*
