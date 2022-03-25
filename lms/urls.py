from django.urls import path

from .views import teachers_list, teacher_classes, lesson_details, lesson_create

app_name = 'lms'

urlpatterns = [
    path('', teachers_list, name='teachers-list'),
    path('<int:teacher_id>/', teacher_classes, name='teacher-classes'),
    path('lesson/<int:lesson_id>/', lesson_details, name='lesson-details'),
    path('class/<int:class_id>/lesson/add/', lesson_create, name='lesson-create')
]