# FitTrack API

A modern fitness tracking application with a RESTful API built with Python and Flask. FitTrack helps users track calories, manage workouts, and achieve their fitness goals with a sleek, gym-inspired interface.

## About

FitTrack combines powerful backend authentication with a stunning, responsive frontend experience. The application handles secure user registration, JWT-based login, password hashing, and data persistence with SQLite, while providing users with an engaging interface to start their fitness journey.

## Tech Stack

### Backend
- **Python** - Core language
- **Flask** - Web framework
- **Flask-SQLAlchemy** - ORM for database management
- **SQLite** - Database storage
- **bcrypt** - Password hashing
- **Flask-JWT-Extended** - JWT authentication tokens
- **Flask-CORS** - Cross-origin resource sharing
- **python-dotenv** - Environment variable management

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with gradients, animations, and responsive design
- **Vanilla JavaScript** - Client-side interactivity
- **Canvas API** - Dynamic background animations

## Project Structure

```
FitTrack-api/
├── database/
│   ├── __init__.py
│   ├── db.py              # Database initialization
│   └── models.py          # User model
├── routes/
│   ├── __init__.py
│   └── auth.py            # Authentication routes
├── static/
│   ├── index.html         # Landing page
│   └── src/
│       ├── js/
│       │   ├── app.js            # Frontend logic
│       │   └── background.js     # Canvas animations
│       └── styles/
│           └── main.css          # Responsive styling
├── instance/
│   └── database.db        # SQLite database
├── .env                   # Environment variables (JWT secret)
├── app.py                 # Application entry point
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
└── README.md
```

## Features

### ✅ Implemented

- **User Registration** - Secure signup with comprehensive validation
- **User Login** - JWT token-based authentication
- **Password Security** - bcrypt hashing with salt
- **Email Validation** - Format checking for valid emails
- **Password Rules** - Minimum 12 characters, special character requirement, no spaces
- **Age Validation** - Integer type checking
- **Database Persistence** - SQLite with SQLAlchemy ORM
- **Duplicate Prevention** - Unique constraints on email and username
- **Protected Routes** - JWT-required endpoints for authorized access
- **Error Handling** - Try/catch blocks with user-friendly messages
- **CORS Support** - Cross-origin requests enabled
- **Responsive Frontend** - Mobile, tablet, and desktop optimized
- **Modern UI/UX** - Gym-inspired design with animations and gradients
- **Dynamic Background** - Canvas-based particle effects

### 🚧 In Development

- Password reset functionality
- User dashboard
- Calorie logging
- Goal weight tracking
- Progress charts
- Workout plans

## Getting Started

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd FitTrack-api
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create .env file**
   ```bash
   echo "JWT_SECRET_KEY=your-secret-key-here" > .env
   ```
   Replace `your-secret-key-here` with a secure random string.

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open in browser**
   - Navigate to `http://127.0.0.1:5000`
   - API available at `http://127.0.0.1:5000`

## API Endpoints

### POST /signup

Creates a new user account with validated data and hashed password.

**Required fields:**

| Field | Type | Description | Validation |
|---|---|---|---|
| name | string | User's full name | Required |
| username | string | Unique username | Required, unique |
| email | string | User's email address | Required, unique, must contain @ and . |
| password | string | Account password | Required, min 12 chars, special char, no spaces |
| ph_number | string | Phone number | Required |
| age | integer | User's age | Required, must be integer |

**Example request:**

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

**Success response:**

```json
{
    "message": "Account has been Created!"
}
```

**Error responses:**

Missing fields:
```json
{
    "error": "['email', 'password'] missing"
}
```

Invalid email:
```json
{
    "error": "Please Enter a valid email."
}
```

Password too short:
```json
{
    "error": "Password must be at least 12 characters long."
}
```

Missing special character:
```json
{
    "error": "Password must contain a special Character !@#$%^&*"
}
```

Duplicate email:
```json
{
    "error": "That email is already registered."
}
```

Duplicate username:
```json
{
    "error": "That username has been taken."
}
```

---

### POST /login

Authenticates a user and returns a JWT access token.

**Required fields:**

| Field | Type | Description |
|---|---|---|
| email | string | User's email address |
| password | string | Account password |

**Example request:**

```json
{
    "email": "alex@example.com",
    "password": "MySecure@Pass123"
}
```

**Success response:**

```json
{
    "message": "You have been logged in!",
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

**Error responses:**

Invalid email:
```json
{
    "error": "Please enter a valid email address."
}
```

Incorrect password:
```json
{
    "error": "Your password is incorrect!!"
}
```

---

### GET /protected

A protected route that requires a valid JWT token.

**Headers:**

```
Authorization: Bearer <your-jwt-token>
```

**Success response:**

```json
{
    "message": "Access granted to protected route!"
}
```

**Error response (no token):**

```json
{
    "msg": "Missing Authorization Header"
}
```

## Frontend Features

- **Landing Page** - Hero section with call-to-action
- **Feature Cards** - Highlighting app capabilities
- **Stats Display** - Active users, pounds lost, success rate
- **Login Page** - User authentication form with token storage
- **Signup Page** - Registration with validation
- **Animated Background** - Dynamic canvas particles and effects
- **Responsive Design** - Optimized for all screen sizes
- **Modern Styling** - Gradients, shadows, and smooth transitions
- **Client-side Validation** - Real-time form feedback

## Security Features

- Password hashing with bcrypt and salt generation
- JWT token-based authentication
- Protected routes requiring valid tokens
- Input validation on both client and server
- SQL injection prevention via SQLAlchemy ORM
- Unique constraints on sensitive fields
- Environment variables for secrets
- Error messages don't expose system details
- CORS configuration for API security

## Configuration

### Database
Database configuration is managed in `config.py`:

```python
SQLALCHEMY_DATABASE_URI = 'sqlite:///instance/database.db'
```

### JWT Secret Key
Set your JWT secret key in `.env`:

```
JWT_SECRET_KEY=your-super-secret-key
```

## Development

The project follows a clean architecture pattern:
- **Separation of concerns** - Routes, models, and database logic are modular
- **Reusable components** - Database and models can be imported anywhere
- **Professional structure** - Industry-standard Flask application layout
- **Environment variables** - Secure configuration management
- **Blueprint routing** - Scalable route organization

## Testing the API

### Register a user:
```bash
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
```

### Login:
```bash
curl -X POST http://127.0.0.1:5000/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "SecurePass@123"
  }'
```

### Access protected route:
```bash
curl -X GET http://127.0.0.1:5000/protected \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

## Contributing

This is a personal learning project, but feedback and suggestions are welcome!

## Project Status

🚀 **Active Development** - Authentication system complete, building out fitness tracking features

## License

MIT License - Feel free to use this project for learning purposes

## Author

Built with 💪 by Cameron
