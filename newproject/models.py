from django.db import models


class Subject(models.Model):
    name = CharField(max_length = 150)
    #schedule = 


class Teacher(models.Model):
    teacher_name = CharField(max_length = 100)
    subject = models.ForeignKey(Subject, on_delete=DO_NOTHING)
    teacher_age = CharField(max_length = 3)


class Student(models.Model):
    student_name = CharField(max_length = 100)
    student_age = CharField(max_length = 3)
    student_class = models.ForeignKey(Class, on_delete=DO_NOTHING)


class Class(models.Model):
    class_name = CharField(max_length = 100)




