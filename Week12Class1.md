
---

# ⭐ **Advanced Django REST Framework (DRF)**

---

# 🔵 **1. Nested Serializers**

Nested serializers are used when you have **related models** and want to include them in a single API response.

### Example Models:

```python
class Course(models.Model):
    name = models.CharField(max_length=100)

class Enrollment(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField(auto_now_add=True)
```

### Nested Serializer:

```python
from rest_framework import serializers

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name']

class EnrollmentSerializer(serializers.ModelSerializer):
    course = CourseSerializer()  # nested serializer

    class Meta:
        model = Enrollment
        fields = ['course', 'date_enrolled']
```

### Include nested enrollments in StudentSerializer:

```python
class StudentSerializer(serializers.ModelSerializer):
    enrollments = EnrollmentSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'grade', 'enrollments']
```

✅ **Result**: Student API now includes all their courses.

---

# 🔵 **2. Advanced ViewSets & Routers**

Use **ModelViewSet** with routers for full CRUD:

```python
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```

### Router:

```python
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')

urlpatterns = router.urls
```

---

# 🔵 **3. Custom Actions in ViewSets**

```python
from rest_framework.decorators import action
from rest_framework.response import Response

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    @action(detail=True, methods=['post'])
    def promote(self, request, pk=None):
        student = self.get_object()
        student.grade = 'Senior'
        student.save()
        return Response({'status': 'student promoted'})
```

* URL: `/students/1/promote/`
* `detail=True` → action for a single object
* `detail=False` → action for the list

---

# 🔵 **4. JWT Authentication**

JWT (JSON Web Token) is widely used for API authentication.

### Install:

```bash
pip install djangorestframework-simplejwt
```

### Settings:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
```

### URL configuration:

```python
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
```

---

# 🔵 **5. Filtering, Searching, and Ordering**

DRF supports powerful query filters:

```python
from rest_framework import viewsets, filters

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'grade']
    ordering_fields = ['age', 'name']
```

* `search_fields` → search using query param `?search=keyword`
* `ordering_fields` → ordering with `?ordering=age`

---

# 🔵 **6. Pagination**

```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
```

* Page 1: `/students/`
* Page 2: `/students/?page=2`

---

# 🔵 **7. Throttling (Rate Limiting)**

Prevent abuse with throttling:

```python
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'user': '10/day',  # 10 requests per day per user
    }
}
```

---

# 🔵 **8. API Versioning**

Support multiple versions:

```python
REST_FRAMEWORK = {
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
}
```

URLs:

```
/api/v1/students/
/api/v2/students/
```

---

# 🔵 **9. Permissions**

Built-in permission classes:

* `AllowAny` → public
* `IsAuthenticated` → logged-in users
* `IsAdminUser` → admin only
* `IsAuthenticatedOrReadOnly` → read-only for unauthenticated users

Custom permission example:

```python
from rest_framework.permissions import BasePermission

class IsAdult(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.age >= 18
```

---

# 🔵 **10. Error Handling & Validation**

### Serializer Validation:

```python
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate_age(self, value):
        if value < 0:
            raise serializers.ValidationError("Age cannot be negative")
        return value
```

### View-level Error Handling:

```python
from rest_framework.response import Response
from rest_framework import status

try:
    student = Student.objects.get(pk=pk)
except Student.DoesNotExist:
    return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
```

---

# 🟢 **Practical Exercises (10–12 Tasks)**

1. Create nested serializers for Student → Enrollment → Course.
2. Build a ModelViewSet with routers for Students.
3. Add a custom action to promote selected students.
4. Implement JWT authentication for the API.
5. Add search and ordering on student fields.
6. Paginate students list to 5 per page.
7. Add throttling: max 5 requests per user per day.
8. Implement a custom permission: only adults can update.
9. Validate age in serializer (no negative age).
10. Add versioning to your API (`v1`, `v2`).
11. Create API for enrollments with nested course info.
12. Write test cases for all API endpoints (GET, POST, PUT, DELETE).

---

