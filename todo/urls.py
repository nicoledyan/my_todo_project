from django.urls import path
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('add/', TaskCreateView.as_view(), name='task_add'),
    path('edit/<int:pk>/', TaskUpdateView.as_view(), name='task_edit'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),
]
