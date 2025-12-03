
from django import forms
from .models import Student

class StudentForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    grade = forms.CharField(max_length=10)
    teacher = forms.CharField(max_length=100)


class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'grade', 'teacher']