# 🧑‍🏫 Teacher Portal - Django Web App

A simple and robust teacher portal web application built using **Django**, **HTML**, **CSS**, and **vanilla JavaScript**. Admins can manage classrooms, teachers, and students. Teachers can register, log in, view and manage their students, and update marks. The app uses a SQLite database and supports clean inline editing, student lookup, and intelligent record updates.

## 🚀 Features

* 🔐 **Teacher Registration & Login Authentication**
* 🧑‍💼 **Admin Dashboard** to manage teachers, classrooms, and students
* 🏫 **Classroom Management**: Add/Edit/Delete classrooms
* 👨‍🏫 **Teacher Management**: Add/Delete teachers, assign classrooms
* 👨‍🎓 **Student Management**: Add/Edit/Delete students by teacher or admin
* ➕ **Smart Student Add**: If a student with the same name and subject exists, new marks are added to existing total
* ✏️ **Inline Editing** of student data (subject and marks)
* 🗑️ **Delete Student** records with confirmation
* 💅 **Modern UI** with custom CSS and responsive modal pop-up forms
* ✅ Built-in Django form protection (`csrf_token`)
* 🛠️ Easy to customize and extend


## 🛠️ Tech Stack

* **Backend**: Python 3.x, Django
* **Frontend**: HTML5, CSS3, JavaScript
* **Database**: SQLite (default)


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

### 3. Create an Admin Teacher

Open Django shell:

```bash
python manage.py shell
```

Then create a user:

```python
from core.models import Teacher
Teacher.objects.create(username='admin', password='admin123', is_admin=True)
exit()
```

### 4. Run the Development Server

```bash
python manage.py runserver
```

Access the application at: [http://127.0.0.1:8000/]


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
│   │   ├── register.html
│   │   ├── home.html
│   │   ├── manage_teachers.html
│   │   └── manage_classrooms.html
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


## 📸 Screenshots (Add Yours)

* ✅ **Login & Register Pages** - clean UI with teacher signup
* 📊 **Dashboard** - shows teachers or students based on role
* 🧾 **Student Listing** - responsive table with edit and delete actions
* ➕ **Add Student Modal** - form with logic to add or update marks
* 🧑‍🏫 **Teacher Management** - admin can add/delete teachers and assign classrooms
* 🏫 **Classroom Management** - admin can create and manage classrooms


## 📈 Future Improvements

* Use Django’s built-in `User` model with password hashing
* Add admin dashboard with charts and statistics
* Integrate Bootstrap or Tailwind for responsive design
* Add pagination and search on student/teacher/classroom tables
* Export data to CSV
* Implement REST APIs for frontend integration
* Add unit and integration tests


