from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import *
from .forms import TodoForm, LoginForm, RegisterForm

# Create your views here.
@login_required(login_url="/login")
def index(request):
    if request.method == "POST":
        form = TodoForm(request.POST)

        if form.is_valid():
            body = request.POST["body"]
            newTodo = Todo.objects.create(author=request.user, body=body)
            newTodo.save()
            return redirect("index")  # Prevents form from resubmitting on refresh
    print(request.user)
    form = TodoForm()
    allTodos = Todo.objects.filter(author=request.user)
    return render(request, "todoForm.html", { "form": form, "todos": allTodos[::-1] })

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            repeat_password = form.cleaned_data.get("repeat_password")
            if password != repeat_password:
                pass
            else:
                user = User.objects.create_user(username=username, password=password)
                login(request, user)
                return redirect("/")
    form = RegisterForm()
    return render(request, "register.html", { "form": form })

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is None:
            form = LoginForm()
            return render(request, "login.html", { "form": form, "error": "Invalid username or password" })
        login(request, user)
        return redirect("/")
    form = LoginForm()
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
