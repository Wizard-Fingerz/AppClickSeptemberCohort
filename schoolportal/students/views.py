from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from .models import Student
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from .forms import StudentForm, StudentModelForm, SignUpForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return HttpResponse("<h1>About the Student Portal</h1>")

def contact(request):
    return HttpResponse("<h1>Contact Us at support@gmail.com")

def profile(request):
    return HttpResponse("<h1>Student Profile Page</h1>")

@login_required(login_url='login')
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


def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            # Access data
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            grade = form.cleaned_data['grade']
            # You can save to DB here manually
            form.save()
            return render(request, 'success.html', {'name': name})
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'reg_form': form})



def add_student(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Automatically saves to DB
            return redirect('student_list')
    else:
        form = StudentModelForm()
    return render(request, 'add_student.html', {'form': form})


def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentModelForm(instance=student)
    return render(request, 'add_student.html', {'form': form})



def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'confirm_delete.html', {'student': student})


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('student-home')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('student-home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('student-home')