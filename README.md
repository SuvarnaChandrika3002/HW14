FastAPI + JWT + BREAD Operations + Playwright E2E Tests

This project implements a full-stack application with:

- FastAPI backend (JWT authentication + CRUD/BREAD)
- Static frontend served via a simple HTTP server
- SQLite database with SQLAlchemy ORM
- Playwright end-to-end (E2E) tests
- Dockerized backend (optional)

### 1. Create and activate a virtual environment
```bash
cd backend
python -m venv .venv
.venv\Scripts\activate      

2. Install dependencies
pip install -r requirements.txt

3. Start FastAPI server
uvicorn main:app --reload


Your API will be available at:

 http://127.0.0.1:8000

 API docs: http://127.0.0.1:8000/docs

 How to Run the Frontend

The frontend is static HTML/JS.
Start a simple HTTP server:

cd forntend
python -m http.server 5500


Frontend available at:

 http://127.0.0.1:5500/forntend/index.html

 http://127.0.0.1:5500/forntend/login.html

 http://127.0.0.1:5500/forntend/register.html

 http://127.0.0.1:5500/forntend/calculations.html

 Running Playwright Tests (E2E)
1. Install Playwright
npm install -D @playwright/test
npx playwright install

2. Ensure both servers are running

Backend:

cd backend
.venv\Scripts\activate
uvicorn main:app --reload


Frontend:

cd forntend
python -m http.server 5500

3. Run tests
cd tests
npx playwright test


To watch tests run in a real browser:

npx playwright test --headed

Docker (Backend Only)
1. Build Docker image
docker build -t your-dockerhub-username/hw14-backend .

2. Run container
docker run -p 8000:8000 your-dockerhub-username/hw14-backend


Backend will be available at:

 http://127.0.0.1:8000/

3. Push to Docker Hub
docker login
docker tag hw14-backend your-dockerhub-username/hw14-backend
docker push your-dockerhub-username/hw14-backend

 Docker Hub Repository Link

Add your Docker Hub repo link here:
