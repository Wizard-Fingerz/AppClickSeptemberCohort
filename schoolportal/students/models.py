from django.db import models
from teachers.models import Teacher

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=250)
    age = models.PositiveIntegerField()
    grade = models.CharField(max_length=10)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='student_profiles/', null=True, blank=True)

    
    def __str__(self):
        return self.name
    
    
    class Meta:
        ordering = ['name']           # Default order
        verbose_name = 'Student Info' # Admin display