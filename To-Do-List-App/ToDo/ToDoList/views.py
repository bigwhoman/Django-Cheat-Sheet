from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *
# Create your views here.
from django.views import generic


# class IndexView(generic.ListView):
#     def get_queryset(self):

def index(request):
    todos = Todo.objects.all()
    if request.method == 'POST':
        todo_title = request.POST['title']
        new_todo = Todo(title=todo_title)
        new_todo.save()
        # return HttpResponseRedirect(reverse('ToDoList:index', args=(todos,)))
        return HttpResponseRedirect('/ToDoList/')
    return render(request, 'ToDoList/index.html', {'todos': todos})
