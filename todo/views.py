from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import Task
from django.views.generic.list import ListView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)


# Create your views here.

class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'todo-list.html'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user,complete=False)

class UpdateListView(UpdateView):
    model=Task
    fields=['subject']
    template_name = 'update-list.html'
    success_url = '/'

class DeleteListView(DeleteView):
    template_name = 'task-confirm-delete.html'
    model = Task
    success_url = '/'

class CreateListView(CreateView):
    model = Task
    fields = ['subject']
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateView, self).form_valid(form)
