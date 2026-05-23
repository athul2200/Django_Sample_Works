# 🐍 Django Sample Works

A collection of Django sample projects demonstrating core web authentication concepts — **Login** and **Registration** — built with Django 6.0.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Projects](#projects)
  - [Login](#login)
  - [Registration](#registration)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [License](#license)

---

## 🔍 Overview

This repository contains standalone Django projects that serve as practical examples for implementing common authentication workflows. Each project is self-contained with its own virtual environment, database, and configuration.

---

## 📂 Projects

### 🔐 Login

A simple login form application built under the **college** project. It demonstrates handling POST requests to capture user credentials (name, username, and password) and rendering a success page upon submission.

**Key Features:**
- Login form with name, username, and password fields
- POST request handling in views
- Success page redirect on form submission
- Integrated with Django's built-in `django.contrib.auth.urls` for authentication routes

**Routes:**
| URL | Description |
|---|---|
| `/` | Login form (home) |
| `/login/` | Login form |
| `/accounts/` | Django built-in auth URLs |
| `/admin/` | Django admin panel |

---

### 📝 Registration

A user registration form application with **server-side validation** using Django Forms. It showcases form creation, field validation, and clean data handling.

**Key Features:**
- Custom `RegisterForm` with name, email, and password fields
- Server-side validation:
  - Name cannot be empty
  - Password must be at least 8 characters
- Django Forms widget usage (`PasswordInput` for password masking)
- Success page on valid registration

**Routes:**
| URL | Description |
|---|---|
| `/` | Home / Index page |
| `/register/` | Registration form |
| `/admin/` | Django admin panel |

---

## 🛠️ Tech Stack

| Technology | Version | Purpose |
|---|---|---|
| **Python** | 3.x | Core language |
| **Django** | 6.0.3 | Web framework |
| **SQLite** | — | Default database |
| **HTML** | 5 | Templates |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+ installed
- `pip` package manager

### Running the Login Project

```bash
# Navigate to the Login project
cd Login/college

# Create & activate virtual environment
python -m venv lenv
lenv\Scripts\activate        # Windows
# source lenv/bin/activate   # macOS/Linux

# Install dependencies
pip install django

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver
```

The app will be available at `http://127.0.0.1:8000/`

### Running the Registration Project

```bash
# Navigate to the Registration project
cd Registration/registration

# Create & activate virtual environment
python -m venv regenv
regenv\Scripts\activate        # Windows
# source regenv/bin/activate   # macOS/Linux

# Install dependencies
pip install django

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver
```

The app will be available at `http://127.0.0.1:8000/`

---

## 🗂️ Project Structure

```
Django/
├── Login/
│   ├── college/                # Django project root
│   │   ├── college/            # Project configuration
│   │   │   ├── settings.py
│   │   │   ├── urls.py
│   │   │   └── wsgi.py
│   │   ├── login/              # Login app
│   │   │   ├── templates/
│   │   │   │   ├── index.html
│   │   │   │   └── success.html
│   │   │   ├── urls.py
│   │   │   └── views.py
│   │   ├── db.sqlite3
│   │   └── manage.py
│   └── lenv/                   # Virtual environment
│
├── Registration/
│   ├── registration/           # Django project root
│   │   ├── registration/       # Project configuration
│   │   │   ├── settings.py
│   │   │   ├── urls.py
│   │   │   └── wsgi.py
│   │   ├── register/           # Register app
│   │   │   ├── templates/
│   │   │   │   ├── index.html
│   │   │   │   ├── register.html
│   │   │   │   └── success.html
│   │   │   ├── forms.py
│   │   │   ├── urls.py
│   │   │   └── views.py
│   │   ├── db.sqlite3
│   │   └── manage.py
│   └── regenv/                 # Virtual environment
│
└── README.md
```

---

## 📄 License

This project is open-source and available for educational purposes.
