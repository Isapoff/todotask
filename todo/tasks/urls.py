from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name="list"),
    path('update_task/<str:pk>/', views.UpdateTask, name="update_task"),
    path('delete_task/<str:pk>/', views.DeleteTask, name="delete_task")
]