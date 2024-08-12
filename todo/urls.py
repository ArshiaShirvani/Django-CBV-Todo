from django.urls import path
from .views import TaskListView,UpdateListView,DeleteListView,CreateListView

app_name="todo"

urlpatterns = [
    path('',TaskListView.as_view(),name='taskview'),
    path('update/<int:pk>',UpdateListView.as_view(),name='updateview'),
    path('delete/<int:pk>',DeleteListView.as_view(),name='deleteview'),
    path('create-task',CreateListView.as_view(),name='createview'),
]