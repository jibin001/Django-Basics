from django.urls import path #type: ignore
from . import views

urlpatterns = [
    path('<int:pk>/', views.employee_detail, name='employee_detail'),
]
