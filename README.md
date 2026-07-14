# 🎓 School API

A RESTful API built with **Django REST Framework** for managing a school system.

This project provides complete CRUD operations for teachers, students, courses, enrollments, and grades using **JWT Authentication**. It also includes **Swagger/OpenAPI documentation**, **Filtering**, **Searching**, **Ordering**, **Pagination**, **Custom Permissions**, and **Automated Tests**.

---

# 🚀 Features

- 🔐 JWT Authentication
- 👨‍🏫 Teacher Management
- 👨‍🎓 Student Management
- 📚 Course Management
- 📝 Enrollment Management
- 🏆 Grade Management
- 🔍 Filtering
- 🔎 Searching
- ↕ Ordering
- 📄 Pagination
- 🔒 Custom Permissions
- 🧪 Automated Tests
- 📘 Swagger / OpenAPI Documentation

---

# 🛠 Technologies

- Python 3.11+
- Django 5
- Django REST Framework
- Simple JWT
- DRF Spectacular
- Django Filter
- SQLite3

---

# 📦 Installation

Clone the repository:

```bash
git clone https://github.com/nascimento140594/school-api.git
```

Navigate to the project directory:

```bash
cd school-api
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Apply database migrations:

```bash
python manage.py migrate
```

Create a superuser:

```bash
python manage.py createsuperuser
```

Run the development server:

```bash
python manage.py runserver
```

The application will be available at:

```
http://127.0.0.1:8000/
```

---

# 🔐 Authentication

The API uses **JWT Authentication**.

Generate an access token:

```http
POST /api/token/
```

Refresh the access token:

```http
POST /api/token/refresh/
```

Use the token in authenticated requests:

```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

---

# 📚 API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/api/teachers/` | Teacher CRUD |
| `/api/students/` | Student CRUD |
| `/api/courses/` | Course CRUD |
| `/api/enrollments/` | Enrollment CRUD |
| `/api/grades/` | Grade CRUD |

---

# 🔎 Filtering

Examples:

```http
GET /api/teachers/?email=john@email.com
```

```http
GET /api/students/?birth_date=2005-04-15
```

```http
GET /api/courses/?teacher=1
```

```http
GET /api/enrollments/?course=1
```

```http
GET /api/grades/?status=PASSED
```

---

# 🔍 Searching

Examples:

```http
GET /api/teachers/?search=john
```

```http
GET /api/students/?search=pedro
```

```http
GET /api/courses/?search=python
```

```http
GET /api/grades/?search=pedro
```

---

# ↕ Ordering

Examples:

```http
GET /api/teachers/?ordering=first_name
```

```http
GET /api/students/?ordering=last_name
```

```http
GET /api/courses/?ordering=name
```

```http
GET /api/grades/?ordering=-score
```

---

# 📄 Pagination

Example:

```http
GET /api/teachers/?page=1
```

---

# 📖 API Documentation

Swagger UI:

```
http://127.0.0.1:8000/api/doc/swagger/
```

OpenAPI Schema:

```
http://127.0.0.1:8000/api/schema/
```

---

# 📷 Screenshots

## 🏠 Home Page

![Home Page](images/home-page.png)

---

## 📘 Swagger UI

![Swagger UI](images/swagger-ui.png)

---

## 🔐 JWT Authentication

![JWT Authentication](images/jwt-authentication.png)

---

## 👨‍🏫 Teachers API

![Teachers API](images/teachers-api.png)

---

## 👨‍🎓 Students API

![Students API](images/students-api.png)

---

## 📚 Courses API

![Courses API](images/courses-api.png)

---

## 📝 Enrollments API

![Enrollments API](images/enrollments-api.png)

---

## 🏆 Grades API

![Grades API](images/grades-api.png)

---

# 🗄 Database Diagram

![Database Diagram](images/database-diagram.png)

---

# 🧪 Running Tests

Run all tests:

```bash
python manage.py test
```

Example output:

```text
Found 9 test(s).

Ran 9 tests in 2.467s

OK
```

---

# 📁 Project Structure

```text
school-api/
│
├── config/
├── school/
│   ├── migrations/
│   ├── tests/
│   ├── admin.py
│   ├── models.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── images/
│   ├── home-page.png
│   ├── swagger-ui.png
│   ├── jwt-authentication.png
│   ├── teachers-api.png
│   ├── students-api.png
│   ├── courses-api.png
│   ├── enrollments-api.png
│   ├── grades-api.png
│   └── database-diagram.png
│
├── templates/
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ✅ Code Quality

The project was validated using:

- flake8
- Django System Check
- Django Migrations Check
- Automated API Tests

Commands:

```bash
python -m flake8

python manage.py check

python manage.py makemigrations --check

python manage.py test
```

---

# 📌 Future Improvements

- Docker support
- PostgreSQL integration
- CI/CD with GitHub Actions
- Increase automated test coverage

---

# 👨‍💻 Author

**Matheus Araújo Nascimento**

📧 Email: **nascimento140594@gmail.com**

🐙 GitHub: https://github.com/nascimento140594

---

## 📄 License

This project was developed for educational and portfolio purposes.
