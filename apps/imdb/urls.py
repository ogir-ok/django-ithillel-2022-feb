from django.urls import path

from apps.imdb.views import MyView, MovieRetrieveUpdateView

app_name = "imdb"

urlpatterns = [
    path("", MyView.as_view()),
    path("<str:pk>/", MovieRetrieveUpdateView.as_view()),
]
