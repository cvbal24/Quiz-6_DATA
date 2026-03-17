# ⚙️ Backend - Home Network & WiFi Setup Platform

## 🏗️ Tech Stack

* Django
* Django REST Framework
* SimpleJWT (Authentication)
* SQLite / PostgreSQL
* Pillow

---

## 🔐 Default Admin Account

```
Email: admin@example.com
Password: admin123
```

⚠️ Or create manually:

```
python manage.py createsuperuser
```

---

## 🚀 Setup Instructions

### 1. Navigate to backend

```
cd backend
```

### 2. Create virtual environment

```
python -m venv venv
source venv/bin/activate
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Setup environment variables

Create `.env` from `.env.sample`

### 5. Run migrations

```
python manage.py makemigrations
python manage.py migrate
```

### 6. Run server

```
python manage.py runserver
```

---

## 🔗 API Routes

```
/api/v1/users/
/api/v1/applications/
/api/v1/services/
/api/v1/orders/
/api/v1/chat/
/api/v1/subscription/
```

---

## 📦 `.env.sample`

```
# DJANGO
SECRET_KEY=your_django_secret_key
DEBUG=True

# DATABASE
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432

# JWT
ACCESS_TOKEN_LIFETIME=60
REFRESH_TOKEN_LIFETIME=1

# PAYPAL
PAYPAL_CLIENT_ID=your_paypal_client_id
PAYPAL_SECRET=your_paypal_secret
PAYPAL_MODE=sandbox

# AI CHATBOT
OPENAI_API_KEY=your_openai_api_key
```

---

## 💳 PayPal Notes

* Multi-merchant setup
* Payments go directly to sellers
* Platform logs transactions only

---
