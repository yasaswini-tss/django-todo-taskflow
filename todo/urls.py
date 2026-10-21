
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),

    path('addTask/', views.addTask, name='addTask'),

    path(
        'completeTask/<int:task_id>/',
        views.completeTask,
        name='completeTask'
    ),

    path(
        'deleteTask/<int:task_id>/',
        views.deleteTask,
        name='deleteTask'
    ),

    path(
        'editTask/<int:task_id>/',
        views.editTask,
        name='editTask'
    ),
]
