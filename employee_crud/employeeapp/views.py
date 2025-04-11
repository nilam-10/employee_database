from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employeeapp/frontend.html', {'employees': employees})

def employee_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        department = request.POST.get('department')
        Employee.objects.create(name=name, email=email, department=department)
        return redirect('employee_list')
    return render(request, 'employeeapp/form.html')

def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.name = request.POST.get('name')
        employee.email = request.POST.get('email')
        employee.department = request.POST.get('department')
        employee.save()
        return redirect('employee_list')
    return render(request, 'employeeapp/form.html', {'employee': employee})

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employeeapp/confirm_delete.html', {'employee': employee})
