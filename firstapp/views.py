
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from firstapp.models import Group, Student, Teacher, Lesson


def teachers_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers_list.html', context={'teachers': teachers})

def teacher_classes(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    groups = Group.objects.filter(teacher=teacher).all()
    print(groups)

    return render(request, 'teachers_classes.html', context={'groups': groups})