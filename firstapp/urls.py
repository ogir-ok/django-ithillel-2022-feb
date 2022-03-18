from django.urls import path

from .views import my_first_view

app_name = 'firstapp'

urlpatterns = [
    path('', my_first_view),
    path('aaaa/', my_first_view)
]