from django.urls import path #type: ignore
from . import views

urlpatterns = [
    path('addTask/', views.addTask, name='addTask')
]
