# 🎓 School API

REST API for school management built with **Django REST Framework**.

This project allows administrators to manage teachers, students, courses, enrollments, and grades through a secure RESTful API with JWT authentication.

---

# 🚀 Features

- Teacher management
- Student management
- Course management
- Student enrollments
- Grade management
- JWT Authentication
- Filtering
- Search
- Ordering
- Pagination
- Swagger Documentation

---

# 🛠 Technologies

- Python 3.11+
- Django 5
- Django REST Framework
- Simple JWT
- drf-spectacular
- django-filter
- SQLite

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/school-api.git
```

Enter the project

```bash
cd school-api
```

Create virtual environment

```bash
python -m venv .venv
```

Activate virtual environment

Windows

```bash
.venv\Scripts\activate
```

Linux / Mac

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run migrations

```bash
python manage.py migrate
```

Create superuser

```bash
python manage.py createsuperuser
```

Run server

```bash
python manage.py runserver
```

---

# 🔐 Authentication

Obtain JWT token

```
POST /api/token/
```

Refresh JWT token

```
POST /api/token/refresh/
```

Authorization header

```
Bearer YOUR_ACCESS_TOKEN
```

---

# 📚 API Endpoints

## Teachers

```
GET     /api/teachers/
POST    /api/teachers/
GET     /api/teachers/{id}/
PUT     /api/teachers/{id}/
PATCH   /api/teachers/{id}/
DELETE  /api/teachers/{id}/
```

---

## Students

```
GET     /api/students/
POST    /api/students/
GET     /api/students/{id}/
PUT     /api/students/{id}/
PATCH   /api/students/{id}/
DELETE  /api/students/{id}/
```

---

## Courses

```
GET     /api/courses/
POST    /api/courses/
GET     /api/courses/{id}/
PUT     /api/courses/{id}/
PATCH   /api/courses/{id}/
DELETE  /api/courses/{id}/
```

---

## Enrollments

```
GET     /api/enrollments/
POST    /api/enrollments/
GET     /api/enrollments/{id}/
PUT     /api/enrollments/{id}/
PATCH   /api/enrollments/{id}/
DELETE  /api/enrollments/{id}/
```

---

## Grades

```
GET     /api/grades/
POST    /api/grades/
GET     /api/grades/{id}/
PUT     /api/grades/{id}/
PATCH   /api/grades/{id}/
DELETE  /api/grades/{id}/
```

---

# 🔎 Filtering

Example

```
GET /api/teachers/?email=john@email.com

GET /api/students/?birth_date=2005-10-10

GET /api/courses/?teacher=1
```

---

# 🔍 Search

Example

```
GET /api/teachers/?search=john

GET /api/students/?search=maria

GET /api/courses/?search=math
```

---

# ↕ Ordering

Example

```
GET /api/teachers/?ordering=last_name

GET /api/students/?ordering=-birth_date

GET /api/grades/?ordering=-score
```

---

# 📖 Swagger Documentation

```
http://127.0.0.1:8000/api/doc/swagger/
```

---

# 📷 Screenshots

Add screenshots here.

Example:

```
docs/images/swagger.png

docs/images/api-root.png

docs/images/teachers.png
```

---

# 🗄 Database Diagram

Add the Draw.io diagram here.

Example

```
docs/database-diagram.png
```

---

# 👨‍💻 Author

Matheus Araujo Nascimento
