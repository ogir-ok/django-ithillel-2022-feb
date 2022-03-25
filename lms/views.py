from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from lms.forms import LessonForm
from lms.models import Group, Lesson

User = get_user_model()


def teachers_list(request):
    teachers = User.objects.filter(is_teacher=True)
    return render(request, 'lms/teachers_list.html', context={'teachers': teachers})


@login_required
def teacher_classes(request, teacher_id):
    teacher = get_object_or_404(User, id=teacher_id, is_teacher=True)
    groups = Group.objects.filter(teacher=teacher).all()

    return render(request, 'lms/teachers_classes.html', context={'groups': groups})


@login_required
def lesson_details(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    return render(request, 'lms/lesson_details.html', context={'lesson': lesson})


@login_required
def lesson_create(request, class_id):

    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            return HttpResponseRedirect(reverse_lazy('lms:lesson-details', kwargs={'lesson_id': lesson.id}))
        return render(request, 'lms/lesson_create.html', context={'form': form})

    form = LessonForm()

    return render(request, 'lms/lesson_create.html', context={'form': form})