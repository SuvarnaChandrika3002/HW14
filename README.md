# Assignment 14: BREAD Endpoints for Calculations

This project implements full BREAD (Browse, Read, Edit, Add, Delete) functionality for user-specific calculations using FastAPI, SQLite, Playwright, and GitHub Actions CI/CD. The goal is to allow authenticated users to perform arithmetic operations, store them in a database, view their history, update entries, and delete records through both backend APIs and frontend interfaces.

## Features

### Backend
- User registration and login with token-based authentication
- SQLAlchemy models for `User` and `Calculation`
- Full BREAD endpoints:
  - GET `/calculations/`
  - GET `/calculations/{id}`
  - POST `/calculations/`
  - PUT `/calculations/{id}`
  - DELETE `/calculations/{id}`
- Automatic recalculation on updates
- Input validation (operation type, divide by zero, numeric fields)

### Frontend
- HTML-based UI with JavaScript fetch calls
- Pages included:
  - `login.html`
  - `register.html`
  - `calculations.html`
  - `new_calculation.html`
  - `edit_calculation.html`
  - `calculation.html`
- Token stored in `localStorage`
- Full CRUD workflow through interface

### Testing
- Playwright end-to-end tests
- Authentication flow tests
- Calculation flow tests (create → browse → read → update → delete)

### CI/CD
GitHub Actions workflow:
- Installs Python and Node.js
- Installs backend and Playwright dependencies
- Starts backend server
- Runs Playwright E2E tests automatically on every push

---

## Setup Instructions

### 1. Install Python dependencies
pip install -r requirements.txt


### 2. Start the backend server
uvicorn app.main:app --reload
Backend will run at:
http://localhost:8000

### 3. Open frontend
Visit:
http://localhost:8000/static/login.html


Create an account, log in, and use the calculations interface.

---

## Run Playwright Tests

### Install Node + Playwright
npm install
npx playwright install


### Start backend
uvicorn app.main:app --port 8000


### Run tests
npx playwright test

### Build


docker-compose build


### Run


docker-compose up


Open:


http://localhost:8000/static/login.html


---

## API Endpoints

### Authentication
| Method | Endpoint        | Description            |
|--------|------------------|------------------------|
| POST   | /users/register  | Create new user        |
| POST   | /users/login     | Get JWT access token   |

### Calculations
| Method | Endpoint               | Description        |
|--------|-------------------------|--------------------|
| GET    | /calculations/         | Browse all entries |
| GET    | /calculations/{id}     | Read one entry     |
| POST   | /calculations/         | Add entry          |
| PUT    | /calculations/{id}     | Edit entry         |
| DELETE | /calculations/{id}     | Delete entry       |

Supported operations:


add
subtract
multiply
divide
