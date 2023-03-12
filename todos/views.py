from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import TodoForm

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
    return render(request, "todoForm.html", { "form": form, "todos": allTodos })
