from django.urls import path

from .views import teachers_list, teacher_classes

app_name = 'firstapp'

urlpatterns = [
    path('', teachers_list, name='teachers-list'),
    path('<int:teacher_id>/', teacher_classes, name='teacher-classes')
]