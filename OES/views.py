from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')

def student(request):
    return render(request, 'student.html')

def teacher(request):
    return render(request, 'teacher.html')