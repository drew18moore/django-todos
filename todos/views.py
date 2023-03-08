from django.shortcuts import render
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
    else:
        form = TodoForm()
    return render(request, "todoForm.html", { "form": form })

def newTodo(request):
    print("NEW TODO")
    body = request.POST["body"]
    newTodo = Todo.objects.create(body=body)
    newTodo.save()
    return HttpResponse("New todo created")
