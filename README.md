# 🐍 Django Sample Works

A collection of Django sample projects demonstrating **Login** and **Registration** authentication workflows, built with Django 6.0.

## 📂 Projects

- **Login** — Simple login form (`Login/college`) with POST request handling and success page redirect.
- **Registration** — User registration form (`Registration/registration`) with server-side validation using Django Forms (name & password validation).

## 🛠️ Tech Stack

Python 3.x · Django 6.0.3 · SQLite · HTML5

## 🚀 Getting Started

```bash
# Navigate to a project (e.g., Login)
cd Login/college

# Create & activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

# Install Django & run
pip install django
python manage.py migrate
python manage.py runserver
```

App runs at `http://127.0.0.1:8000/`

## 📄 License

Open-source — available for educational purposes.
