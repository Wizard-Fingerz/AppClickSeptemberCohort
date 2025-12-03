
---

# ⭐ **DJANGO REST FRAMEWORK (DRF) — Comprehensive Guide**

Django REST Framework is a **powerful toolkit** to build web APIs in Django. It allows developers to expose Django models and logic as RESTful endpoints.

---

# 🔵 **1. Installing DRF**

```bash
pip install djangorestframework
```

Add to `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    ...,
    'rest_framework',
]
```

Optional: Add default authentication in `settings.py`:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ]
}
```

---

# 🔵 **2. Creating a Simple API**

Suppose we have a `Student` model:

```python
# models.py
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    grade = models.CharField(max_length=10)
```

---

## **Step 1 — Create Serializer**

Serializers convert model instances into **JSON**.

```python
# serializers.py
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
```

---

## **Step 2 — Create API Views**

### Option 1: Using `APIView`

```python
# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer

class StudentList(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

---

### Option 2: Using `GenericAPIView` + Mixins

```python
from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer

class StudentListCreate(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```

✅ This is **shorter** and DRY.

---

### Option 3: Using `ViewSets`

```python
from rest_framework import viewsets

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```

---

# 🔵 **3. URL Routing for APIs**

### Option 1: Standard URLs

```python
from django.urls import path
from .views import StudentList

urlpatterns = [
    path('students/', StudentList.as_view(), name='student-list'),
]
```

---

### Option 2: Using Routers with ViewSets

```python
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')

urlpatterns = router.urls
```

---

# 🔵 **4. CRUD Operations in DRF**

| Operation | HTTP Method | URL Example  | View                                |
| --------- | ----------- | ------------ | ----------------------------------- |
| Create    | POST        | /students/   | ListCreateAPIView or ViewSet.create |
| Read all  | GET         | /students/   | ListAPIView or ViewSet.list         |
| Read one  | GET         | /students/1/ | RetrieveAPIView or ViewSet.retrieve |
| Update    | PUT/PATCH   | /students/1/ | UpdateAPIView or ViewSet.update     |
| Delete    | DELETE      | /students/1/ | DestroyAPIView or ViewSet.destroy   |

---

# 🔵 **5. Permissions and Authentication**

### Built-in permissions:

```python
from rest_framework.permissions import IsAuthenticated, AllowAny

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]  # Only logged-in users can access
```

### Token Authentication:

```bash
pip install djangorestframework-simplejwt
```

---

# 🔵 **6. Filtering and Searching**

### Filtering:

```python
from rest_framework import viewsets, filters

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'grade']
    ordering_fields = ['age', 'name']
```

---

### URL Example:

```
GET /students/?search=Adewale
GET /students/?ordering=age
```

---

# 🔵 **7. Pagination**

Add pagination in `settings.py`:

```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5,
}
```

API automatically returns **5 items per page**.

---

# 🔵 **8. Response Customization**

You can modify responses:

```python
def get(self, request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response({
        "status": "success",
        "data": serializer.data,
        "count": students.count()
    })
```

---

# 🔵 **9. Error Handling**

DRF automatically handles:

* 400 → Validation errors
* 404 → Object not found
* 401 → Unauthorized

You can customize:

```python
from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        response.data['status_code'] = response.status_code
    return response
```

---

# 🔵 **10. Testing DRF APIs**

You can use:

* Browser API interface
* Postman / Insomnia
* Django test client:

```python
from rest_framework.test import APITestCase
from django.urls import reverse

class StudentAPITest(APITestCase):
    def test_list_students(self):
        url = reverse('student-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
```

---

# 🔵 **11. Practical Exercises (10–12 Tasks)**

1. Build a DRF API for `Student` model with full CRUD.
2. Implement token authentication for API access.
3. Add search functionality on `name` and `grade`.
4. Implement ordering by `age` and `name`.
5. Add pagination with 5 students per page.
6. Customize API response to include `status` and `count`.
7. Add filtering to get only students above age 18.
8. Create a custom exception handler to include `status_code` in errors.
9. Use `ViewSets` and routers instead of `APIView`.
10. Write test cases for all API endpoints.
11. Add a nested serializer to show enrollments for each student.
12. Secure the API using `IsAuthenticated` permission.

---

