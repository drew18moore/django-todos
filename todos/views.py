from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import *
from .forms import TodoForm, LoginForm, RegisterForm

# Create your views here.
def index(request):
    if request.method == "POST":
        form = TodoForm(request.POST)

        if form.is_valid():
            body = request.POST["body"]
            newTodo = Todo.objects.create(body=body)
            newTodo.save()
            return redirect("index")  # Prevents form from resubmitting on refresh
    form = TodoForm()
    allTodos = Todo.objects.all()
    return render(request, "todoForm.html", { "form": form, "todos": allTodos[::-1] })

def register(request):
    if request.method == "POST":
        return redirect("register")
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

def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect("index")
