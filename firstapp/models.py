from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateField()

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=255)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, null=True)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    group = models.ForeignKey(Group, on_delete=models.PROTECT, null=True,
                              related_name='lessons')

    def __str__(self):
        return self.name