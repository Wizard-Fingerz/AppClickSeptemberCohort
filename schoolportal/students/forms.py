
from django import forms
from .models import Student
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class StudentForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    grade = forms.CharField(max_length=10)
    teacher = forms.CharField(max_length=100)

    def clean_age(self):
        age = self.cleaned_data['age']

        if age < 18:
            raise forms.ValidationError("Age must be at least 18.")
        return age


class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'grade', 'teacher', 'profile_picture']

    def clean_age(self):
        age = self.cleaned_data['age']

        if age < 18:
            raise forms.ValidationError("Age must be at least 18.")
        return age

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
