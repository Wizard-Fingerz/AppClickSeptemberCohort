
---

# ⭐ **Full DRF Project: School Management API**

### Features we will implement:

1. Students CRUD
2. Courses CRUD
3. Enrollments CRUD
4. JWT Authentication
5. Nested serializers for enrollments inside students
6. Permissions
7. Pagination
8. Caching of list endpoints

---

# 🔵 **1. Project Setup**

```bash
django-admin startproject school_api
cd school_api
python manage.py startapp students
pip install djangorestframework djangorestframework-simplejwt django-redis
```

Add to `settings.py`:

```python
INSTALLED_APPS = [
    ...,
    'rest_framework',
    'students',
]

# JWT
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5,
}

# Redis Caching
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
```

---

# 🔵 **2. Models**

```python
# students/models.py
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    grade = models.CharField(max_length=10)

class Course(models.Model):
    name = models.CharField(max_length=100)

class Enrollment(models.Model):
    student = models.ForeignKey(Student, related_name='enrollments', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='enrollments', on_delete=models.CASCADE)
    date_enrolled = models.DateField(auto_now_add=True)
```

```bash
python manage.py makemigrations
python manage.py migrate
```

---

# 🔵 **3. Serializers**

```python
# students/serializers.py
from rest_framework import serializers
from .models import Student, Course, Enrollment

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name']

class EnrollmentSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Enrollment
        fields = ['id', 'course', 'date_enrolled']

class StudentSerializer(serializers.ModelSerializer):
    enrollments = EnrollmentSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'grade', 'enrollments']

    def validate_age(self, value):
        if value < 0:
            raise serializers.ValidationError("Age cannot be negative")
        return value
```

---

# 🔵 **4. Views (ViewSets + JWT Permissions)**

```python
# students/views.py
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.core.cache import cache
from .models import Student, Course, Enrollment
from .serializers import StudentSerializer, CourseSerializer, EnrollmentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'grade']
    ordering_fields = ['age', 'name']

    # Nested Caching for list
    def list(self, request, *args, **kwargs):
        cached_data = cache.get('students_list')
        if cached_data:
            return Response(cached_data)
        response = super().list(request, *args, **kwargs)
        cache.set('students_list', response.data, 60)  # cache 60 seconds
        return response

    @action(detail=True, methods=['post'])
    def promote(self, request, pk=None):
        student = self.get_object()
        student.grade = 'Senior'
        student.save()
        cache.delete('students_list')  # invalidate cache
        return Response({'status': 'student promoted'})

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]
```

---

# 🔵 **5. URLs & Routers**

```python
# students/urls.py
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, CourseViewSet, EnrollmentViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'enrollments', EnrollmentViewSet, basename='enrollment')

urlpatterns = [
    path('', include(router.urls)),
]
```

### JWT URLs:

```python
# school_api/urls.py
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/', include('students.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
```

---

# 🔵 **6. Testing the API**

* **Get JWT token**: POST `/api/token/` with username & password
* **Access protected endpoints**:
  `Authorization: Bearer <token>`
* **List students**: GET `/api/students/` → cached for 60 seconds
* **Promote student**: POST `/api/students/{id}/promote/`
* **Search students**: `/api/students/?search=Adewale`
* **Order students**: `/api/students/?ordering=age`
* **Pagination**: `/api/students/?page=2`

---

# 🔵 **7. Summary of Features Integrated**

| Feature                          | How Implemented                                     |
| -------------------------------- | --------------------------------------------------- |
| JWT Authentication               | `rest_framework_simplejwt`                          |
| Nested Serializers               | `StudentSerializer` includes `EnrollmentSerializer` |
| Permissions                      | `IsAuthenticatedOrReadOnly` & `IsAuthenticated`     |
| Pagination                       | `DEFAULT_PAGINATION_CLASS` in settings              |
| Caching                          | `cache.get` / `cache.set` in `StudentViewSet`       |
| Filtering / Searching / Ordering | DRF `filters.SearchFilter`, `OrderingFilter`        |
| Custom Actions                   | `promote` method with `@action` decorator           |

---

# 🟢 **8. Suggested Practical Exercises**

1. Add **user registration** endpoint with JWT token returned.
2. Add **email notification** on student promotion.
3. Cache **courses list** for 2 minutes.
4. Implement **nested enrollments under course** in CourseSerializer.
5. Add **custom permissions**: only admins can delete enrollments.
6. Extend JWT to include **user role** in token payload.
7. Test **pagination** for students API with 5 per page.
8. Implement **throttling**: 10 requests per user per minute.
9. Add **soft delete** for students (mark inactive instead of deleting).
10. Write **unit tests** for all endpoints (JWT auth, CRUD, cache, permissions).

---
