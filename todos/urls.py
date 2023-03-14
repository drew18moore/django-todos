from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("todo/<int:todo_id>/delete/", views.delete_todo, name="delete_todo"),
]
