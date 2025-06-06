
# 🧑‍🏫 Teacher Portal - Django Web App

A simple and robust teacher portal web application built using **Django**, **HTML**, **CSS**, and **vanilla JavaScript**. Teachers can log in, view and manage students, and update student marks. The app uses a SQLite database and supports clean inline editing, student lookup, and dynamic addition of records.

---

## 🚀 Features

- 🔐 **Teacher Login Authentication**
- 📋 **Student Listing** with name, subject, and marks
- ✏️ **Inline Editing** of student data
- 🗑️ **Delete Student** records
- ➕ **Add New Student** with logic to update marks if student already exists
- 💅 **Modern UI** with custom CSS and modal pop-up form
- ✅ Built-in Django form protection (`csrf_token`)
- 🛠️ Easy to customize and extend

---

## 🛠️ Tech Stack

- **Backend**: Python 3.x, Django
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite (default)

---

## 🏁 Getting Started


### 1. Install Requirements

Make sure you have Python installed (Python 3.9 or newer). Then install Django:

```bash
pip install django
```

### 2. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Create a Teacher User

Open Django shell:

```bash
python manage.py shell
```

Then create a user:

```python
from core.models import Teacher
Teacher.objects.create(username='admin', password='admin123')
exit()
```

### 4. Run the Development Server

```bash
python manage.py runserver
```

Access the application at: http://127.0.0.1:8000/

---

## 📂 Project Structure

```
teacher_portal/
├── core/
│   ├── migrations/
│   ├── static/core/
│   │   ├── style.css
│   │   └── scripts.js
│   ├── templates/core/
│   │   ├── login.html
│   │   └── home.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
├── teacher_portal/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── README.md
```

---

## 📸 Screenshots (Add Yours)

- ✅ **Login Page** - centered form with styled container
- 📊 **Student Listing Page** - responsive table, inline update/delete buttons
- ➕ **Add Student Modal** - popup with validation

---

## 📈 Future Improvements

- Use Django’s built-in `User` model with password hashing
- Add admin dashboard with more statistics
- Integrate Bootstrap or Tailwind for better responsiveness
- Add pagination and search on student table
- Export student data to CSV
- Add unit tests and REST API

---

