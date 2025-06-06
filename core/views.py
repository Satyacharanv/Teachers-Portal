from django.shortcuts import render, redirect
from .models import Teacher, Student
from django.contrib import messages
from .models import Classroom
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.shortcuts import redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            teacher = Teacher.objects.get(username=username, password=password)
            request.session['teacher_id'] = teacher.id
            return redirect('home')
        except Teacher.DoesNotExist:
            messages.error(request, 'Invalid credentials')
    return render(request, 'core/login.html')

def home_view(request):
    if 'teacher_id' not in request.session:
        return redirect('login')
    classrooms = Classroom.objects.all()

    teacher = Teacher.objects.get(id=request.session['teacher_id'])

    if teacher.username == 'admin':
        students = Student.objects.all()
        teachers = Teacher.objects.exclude(username='admin')
    else:
        students = Student.objects.filter(classroom=teacher.classroom)
        teachers = None  # Hide teachers for non-admins

    return render(request, 'core/home.html', {
        'students': students,
        'teachers': teachers,
        'current_teacher': teacher,
        'classrooms': classrooms
    })

def add_student(request):
    if 'teacher_id' not in request.session:
        return redirect('login')

    teacher = Teacher.objects.get(id=request.session['teacher_id'])

    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        marks = int(request.POST['marks'])

        try:
            student = Student.objects.get(name=name, subject=subject, classroom=teacher.classroom)
            student.marks += marks
            student.save()
        except Student.DoesNotExist:
            Student.objects.create(
                name=name,
                subject=subject,
                marks=marks,
                classroom=teacher.classroom
            )

    return redirect('home')

def update_student(request, id):
    if request.method == 'POST' and 'teacher_id' in request.session:
        teacher = Teacher.objects.get(id=request.session['teacher_id'])
        student = Student.objects.get(id=id)
        # Admin can update any student, others only their classroom
        if teacher.username == 'admin' or student.classroom == teacher.classroom:
            student.name = request.POST['name']
            student.subject = request.POST['subject']
            student.marks = request.POST['marks']
            student.save()
    return redirect('home')

def delete_student(request, id):
    if 'teacher_id' in request.session:
        teacher = Teacher.objects.get(id=request.session['teacher_id'])
        student = Student.objects.get(id=id)
        # Admin can delete any student, others only their classroom
        if teacher.username == 'admin' or student.classroom == teacher.classroom:
            student.delete()
    return redirect('home')



def register_view(request):
    classrooms = Classroom.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        classroom_id = request.POST['classroom']

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
        elif Teacher.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        else:
            classroom = Classroom.objects.get(id=classroom_id)
            Teacher.objects.create(username=username, password=password, classroom=classroom)
            messages.success(request, "Registration successful. Please log in.")
            return redirect('login')

    return render(request, 'core/register.html', {'classrooms': classrooms})

def is_admin(request):
    return request.session.get('is_admin') == True


def manage_classrooms(request):
    if 'teacher_id' not in request.session:
        return redirect('login')

    teacher = Teacher.objects.get(id=request.session['teacher_id'])
    if teacher.username != 'admin':
        messages.error(request, "Access denied: only admin can add classrooms.")
        return redirect('home')

    if request.method == 'POST':
        name = request.POST['name']
        if not Classroom.objects.filter(name=name).exists():
            Classroom.objects.create(name=name)
            messages.success(request, f'Classroom "{name}" added.')
        else:
            messages.error(request, "Classroom already exists.")

    classrooms = Classroom.objects.all()
    return render(request, 'core/manage_classrooms.html', {'classrooms': classrooms})

def manage_teachers(request):
    if 'teacher_id' not in request.session:
        return redirect('login')

    teacher = Teacher.objects.get(id=request.session['teacher_id'])
    if teacher.username != 'admin':
        messages.error(request, "Access denied: only admin can manage teachers.")
        return redirect('home')

    teachers = Teacher.objects.exclude(username='admin')
    classrooms = Classroom.objects.all()
    return render(request, 'core/manage_teachers.html', {
        'teachers': teachers,
        'classrooms': classrooms
    })

def update_teacher(request, id):
    if 'teacher_id' not in request.session:
        return redirect('login')

    current_teacher = Teacher.objects.get(id=request.session['teacher_id'])
    if current_teacher.username != 'admin':
        messages.error(request, "Access denied: only admin can update teacher details.")
        return redirect('home')

    if request.method == 'POST':
        teacher = Teacher.objects.get(id=id)
        teacher.username = request.POST['username']
        teacher.classroom_id = request.POST['classroom']
        teacher.save()
        messages.success(request, "Teacher updated successfully.")
    return redirect('manage_teachers')

def delete_teacher(request, id):
    if 'teacher_id' not in request.session:
        return redirect('login')

    current_teacher = Teacher.objects.get(id=request.session['teacher_id'])
    if current_teacher.username != 'admin':
        messages.error(request, "Access denied: only admin can delete teachers.")
        return redirect('home')

    teacher = Teacher.objects.get(id=id)
    if teacher.username == 'admin':
        messages.error(request, "Cannot delete the admin account.")
    else:
        teacher.delete()
        messages.success(request, "Teacher deleted successfully.")

    return redirect('manage_teachers')
