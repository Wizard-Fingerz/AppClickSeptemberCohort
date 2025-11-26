from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100, choices=[
        ('Math', 'Mathematics'),
        ('Sci', 'Science'),
        ('Eng', 'English'),
        ('Hist', 'History'),
    ])
    email = models.EmailField(unique=True)
    joined_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.email