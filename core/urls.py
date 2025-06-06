from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('add/', views.add_student, name='add_student'),
    path('update/<int:id>/', views.update_student, name='update_student'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),
    path('register/', views.register_view, name='register'),
    path('manage_classrooms/', views.manage_classrooms, name='manage_classrooms'),
    path('manage_teachers/', views.manage_teachers, name='manage_teachers'),
    path('update_teacher/<int:id>/', views.update_teacher, name='update_teacher'),
    path('delete_teacher/<int:id>/', views.delete_teacher, name='delete_teacher'),
]
