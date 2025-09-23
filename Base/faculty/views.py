from django.shortcuts import render, get_object_or_404
from .models import Department, Program, Teacher, MainPageContent

def home(request):
    content = MainPageContent.objects.first()
    return render(request, 'faculty/home.html', {'content': content})

def program_list(request):
    programs = Program.objects.all()
    return render(request, 'faculty/program_list.html', {'programs': programs})

def program_detail(request, pk):
    program = get_object_or_404(Program, pk=pk)
    return render(request, 'faculty/program_detail.html', {'program': program})

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'faculty/department_list.html', {'departments': departments})

def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    teachers = Teacher.objects.filter(department=department)
    programs = department.programs.all()
    return render(request, 'faculty/department_detail.html', {
        'department': department,
        'teachers': teachers,
        'programs': programs,
    })
