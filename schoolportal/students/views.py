from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Student
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.


def home(request):
    return HttpResponse("<h1>Welcome to the Student Portal</h1>")


def about(request):
    return HttpResponse("<h1>About the Student Portal</h1>")

def contact(request):
    return HttpResponse("<h1>Contact Us at support@gmail.com")

def profile(request):
    return HttpResponse("<h1>Student Profile Page</h1>")

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'all_students': students})


def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'student_detail.html', {'student': student})


class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello from Class-Based View!")
    

class HomePageView(TemplateView):
    template_name = 'home.html'



class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'all_students'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_detail.html'
    context_object_name = 'student'
