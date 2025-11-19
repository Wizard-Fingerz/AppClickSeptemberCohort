from django.urls import path
from .views import home, about, contact, profile, student_list, student_detail, HelloView, HomePageView, StudentListView, StudentDetailView


urlpatterns = [
    path('', home, name='student-home'),
    path('about/', about, name='student-about'),
    path('contact/', contact, name='student-contact'),
    path('profile/', profile, name='student-profile'),
    path('student_list/', student_list, name='student_list'),
    path('student_detail/<int:student_id>/', student_detail, name='student_detail'),
    path('hello/', HelloView.as_view(), name='hello'),
    path('homepage/', HomePageView.as_view(), name='home-page'),
    path('students/', StudentListView.as_view(), name='student-list'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='student_detail')



]