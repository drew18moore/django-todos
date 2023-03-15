from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("register", views.register_view, name="register"),
    path("logout", views.logout_view, name="logout"),
    path("todo/<int:todo_id>/delete/", views.delete_todo, name="delete_todo"),
    path("todo/<int:todo_id>/check/", views.check_todo, name="check_todo"),
]
