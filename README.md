# Traders Portal – Django Backend

A secure, scalable backend service for managing user watchlists of stocks. Built with **Django**, **Django REST Framework (DRF)**, and **PostgreSQL**, this service supports JWT authentication, company filtering, and full watchlist management.

---

## 🚀 Features

- ✅ **JWT Authentication** – Secure user registration and login
- ✅ **Company Management** – Browse, search, and filter companies
- ✅ **Watchlist CRUD** – Add, remove, and view watched stocks
- ✅ **Search & Filter** – Query companies by name, sector, and industry
- ✅ **Docker Support** – Local and production-ready containerization
- ✅ **API Documentation** – Interactive Swagger UI for easy testing

---

## 🛠️ Tech Stack

- **Backend**: Python, Django, Django REST Framework
- **Database**: PostgreSQL (with SQLite fallback)
- **Authentication**: JWT via `djangorestframework-simplejwt`
- **Search & Filter**: `django-filter`
- **API Docs**: `drf-yasg` (Swagger UI)
- **Deployment**: Docker, Docker Compose

---

## 📦 Setup Instructions

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/traders-portal.git](https://github.com/tarun2512/tradebrains-assignment-django.git)
cd traders-portal

# Database Settings
DB_NAME=traders_db
DB_USER=postgres
DB_PASSWORD=trade123
DB_HOST=localhost
DB_PORT=5432

# Django Settings
SECRET_KEY=django-insecure-xyz1234567890
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations companies
python manage.py makemigrations watchlist
python manage.py migrate

# Load company data from CSV
python manage.py load_companies master.csv

# Start the development server
python manage.py runserver

#Debugging(Optional)
python manage.py shell

```
## APIs
- `POST /api/register/` - Register user
- `POST /api/login/` - Get JWT tokens
- `GET /api/companies/?name=Apple&sector=Tech` - Search
- `GET /api/watchlist/` - View watchlist
- `POST /api/watchlist/add/` - `{ "symbol": "AAPL" }`
- `POST /api/watchlist/remove/` - `{ "symbol": "AAPL" }`

## Docs
Visit: http://localhost:8000/swagger/















