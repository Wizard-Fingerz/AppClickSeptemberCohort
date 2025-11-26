from django.urls import path
from .views import *

urlpatterns = [
    path('teacher_home/', teacher_home, name='teacher-home'),


]