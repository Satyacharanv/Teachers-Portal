from django.db import models

class Classroom(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=150)
    classroom = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.username

class Student(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    marks = models.IntegerField()
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.subject}"
