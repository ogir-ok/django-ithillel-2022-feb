from django import forms

from lms.models import Lesson


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['name', 'date', 'description']