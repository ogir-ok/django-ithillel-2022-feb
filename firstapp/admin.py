from django.contrib import admin

# Register your models here.
from firstapp.models import Student, Teacher, Group, Lesson


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birth_date')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birth_date')


class LessonInline(admin.StackedInline):
    model = Lesson


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', )
    inlines = (LessonInline, )


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')