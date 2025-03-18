from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from django.contrib import messages


# Create your views here.

def index(request):
    students= Student.objects.all()
    return render(request, 'index.html',{'students':students})

def about(request):
    return render(request, 'about.html')


def form(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        email = request.POST['email']

        # Save to the database
        student = Student(name=name, age=age, email=email)
        student.save()
        # Display a success message
        messages.success(request, "Student registered successfully!")
        return redirect('index')  # Redirect to the same page or another view
    return render(request, 'index.html')

def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.age = request.POST.get('age')
        student.email = request.POST.get('email')
        student.save()
        messages.success(request, "Student updated successfully!")
    return redirect('index')

def delete_student(request, id):
    student = Student.objects.get(id=id)
    # Delete from the database
    student.delete()
    # Display a success message
    messages.success(request, "Student deleted successfully!")
    return redirect('index')  # Redirect to the same page or another view
