from django.urls import path
from .views import home, about, contact, profile


urlpatterns = [
    path('', home, name='student-home'),
    path('about/', about, name='student-about'),
    path('contact/', contact, name='student-contact'),
    path('profile/', profile, name='student-profile'),
]