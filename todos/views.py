from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse
from .models import *
from .forms import TodoForm, LoginForm, RegisterForm

# Create your views here.
@login_required(login_url="/login")
def index(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        body = form.cleaned_data.get("body")
        newTodo = Todo.objects.create(author=request.user, body=body)
        newTodo.save()
        return redirect("index")  # Prevents form from resubmitting on refresh
    allTodos = Todo.objects.filter(author=request.user)
    return render(request, "todoForm.html", { "form": form, "todos": allTodos[::-1] })

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        repeat_password = form.cleaned_data.get("repeat_password")
        if password != repeat_password:
            return render(request, "register.html", { "form": form, "error": "Passwords do not match" })
        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return render(request, "register.html", { "form": form, "error": "Username already exists" })
        login(request, user)
        return redirect("/")
    return render(request, "register.html", { "form": form })

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is None:
            form = LoginForm()
            return render(request, "login.html", { "form": form, "error": "Invalid username or password" })
        login(request, user)
        return redirect("/")
    return render(request, "login.html", { "form": form })

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/login")
    return HttpResponse({"message": "logout_view"})

def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect("index")
