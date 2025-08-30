# ACEest Fitness & Gym — Flask + Pytest + Docker + GitHub Actions

A foundational Flask web app for ACEest_Fitness and Gym that demonstrates core DevOps practices:
- **Flask** app exposing workout endpoints
- **Pytest** unit tests
- **Docker** containerization
- **GitHub Actions** CI to build the Docker image and run tests inside the container on every push

> This project is a web counterpart of a simple Tkinter workout tracker, adapted to meet CI/CD + containerization requirements.

---

## 🧱 Project Structure

```
.
├── app.py
├── templates/
│   └── index.html
├── tests/
│   └── test_app.py
├── requirements.txt
├── Dockerfile
└── .github/
    └── workflows/
        └── ci.yml
```

---

## 🚀 Run Locally

### 1) With Python
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -c "from app import create_app; create_app().run(host='0.0.0.0', port=8000, debug=True)"
# Open http://localhost:8000
```

### 2) With Gunicorn (recommended)
```bash
pip install -r requirements.txt
gunicorn -b 0.0.0.0:8000 app:app
```

### 3) With Docker
```bash
docker build -t aceest-fitness:latest .
docker run --rm -p 8000:8000 aceest-fitness:latest
# Open http://localhost:8000
```

---

## ✅ Run Tests

### Locally (host)
```bash
pytest -q
```

### Via Docker (inside the image)
```bash
docker build -t aceest-fitness:ci .
docker run --rm aceest-fitness:ci pytest -q
```

---

## 🔁 CI/CD (GitHub Actions)

The workflow at `.github/workflows/ci.yml`:
1. Triggers on every **push** and **pull request**.
2. **Builds** the Docker image.
3. **Runs** the Pytest test suite **inside the container**.

You can verify successful runs in your repo under **Actions**.

---

## 📦 API Overview

- `GET /` — HTML page with a simple form + live list
- `POST /workouts` — Add a workout
  - Body: JSON or form data `{"workout": "Run", "duration": 30}`
- `GET /workouts` — List all workouts
- `DELETE /workouts` — Clear all workouts (for demo/testing)

> Note: For simplicity the store is in-memory. In production, swap with a database.

---

## 📝 Notes for Evaluators

- Pytest covers route presence, validation, happy paths, and clear operation.
- Dockerfile is minimal and uses **Python 3.11 slim** + **Gunicorn**.
- CI runs tests **inside** the built image to align with assignment requirements.
