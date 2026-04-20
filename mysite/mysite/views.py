from django.http import HttpResponse #type: ignore
from django.shortcuts import render #type: ignore
from employees.models import Employee

def home(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees,
    }
    return render(request, 'home.html', context)