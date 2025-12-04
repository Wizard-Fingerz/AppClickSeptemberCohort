from django.urls import path
from .views import home, about, contact, profile, update_student, register, login_view, logout_view,add_student, delete_student, student_list, student_form,student_detail, HelloView, HomePageView, StudentListView, StudentDetailView


urlpatterns = [
    path('', home, name='student-home'),
    path('about/', about, name='student-about'),
    path('contact/', contact, name='student-contact'),
    path('profile/', profile, name='student-profile'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('student_list/', student_list, name='student_list'),
    path('student_detail/<int:student_id>/', student_detail, name='student_detail'),
    path('hello/', HelloView.as_view(), name='hello'),
    path('homepage/', HomePageView.as_view(), name='home-page'),
    path('students/', StudentListView.as_view(), name='student-list'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('student_form/', student_form, name='student_form'),
    path('student_model_form/', add_student, name='student_model_form'),
    path('update_student/<int:id>/', update_student, name='student_update'),
    path('delete_student/<int:id>', delete_student, name='student_delete')



]