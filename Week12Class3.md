
---

# ⭐ **API Documentation & Testing with Swagger in Django REST Framework**

Swagger (now known as **OpenAPI**) allows developers and consumers to:

* Explore your API endpoints
* See request/response schemas
* Test endpoints interactively in the browser

Django REST Framework supports Swagger through **drf-yasg** and **drf-spectacular**. We'll focus on **drf-yasg**, which is very popular.

---

# 🔵 **1. Install drf-yasg**

```bash
pip install drf-yasg
```

Add to `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    ...,
    'drf_yasg',
]
```

---

# 🔵 **2. Add Swagger URLs**

In your project `urls.py`:

```python
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="School Management API",
        default_version='v1',
        description="API documentation for School Management project",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="admin@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Your existing URLs
    path('api/', include('students.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Swagger URLs
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
```

---

# 🔵 **3. Access Swagger UI**

Run the server:

```bash
python manage.py runserver
```

Visit:

* **Swagger UI:** `http://127.0.0.1:8000/swagger/`
* **ReDoc UI:** `http://127.0.0.1:8000/redoc/`
* **JSON/YAML Schema:** `http://127.0.0.1:8000/swagger.json`

Swagger UI allows **interactive testing**: you can send GET, POST, PUT, DELETE requests directly from the browser.

---

# 🔵 **4. Annotating Endpoints**

Swagger automatically generates documentation from DRF serializers and viewsets. You can **add descriptions** for more clarity.

### Example:

```python
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    @swagger_auto_schema(
        operation_description="Promote a student to the next grade",
        responses={200: StudentSerializer(many=False)}
    )
    @action(detail=True, methods=['post'])
    def promote(self, request, pk=None):
        student = self.get_object()
        student.grade = 'Senior'
        student.save()
        return Response({'status': 'student promoted'})
```

* `swagger_auto_schema` allows **custom descriptions, response schemas, and manual parameters**.

---

# 🔵 **5. Documenting Query Parameters**

For endpoints that use **filters, search, or ordering**, you can define query parameters.

```python
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class StudentViewSet(viewsets.ModelViewSet):
    ...
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('search', openapi.IN_QUERY, description="Search by name or grade", type=openapi.TYPE_STRING),
            openapi.Parameter('ordering', openapi.IN_QUERY, description="Order by age or name", type=openapi.TYPE_STRING)
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
```

---

# 🔵 **6. Documenting JWT Authentication**

Swagger can include JWT authentication:

```python
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="School Management API",
        default_version='v1',
        description="API documentation with JWT Authentication",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Add security definitions automatically
```

* In Swagger UI, click **Authorize** and enter JWT token:

  ```
  Bearer <your_token_here>
  ```

---

# 🔵 **7. Benefits of Swagger Integration**

✅ Easy **testing and exploration** of APIs
✅ Automatically generated **request/response documentation**
✅ Interactive **UI for front-end developers**
✅ Can export **OpenAPI specification** (JSON/YAML)
✅ Can be used for **client SDK generation**

---

# 🟢 **8. Suggested Exercises**

1. Add Swagger documentation to **all endpoints** in your School API.
2. Annotate custom actions like `promote` with descriptions.
3. Include JWT authentication in Swagger UI.
4. Add query parameters for search and ordering.
5. Use `swagger_auto_schema` to document POST request bodies.
6. Create ReDoc UI and compare with Swagger UI.
7. Export your API schema as JSON and YAML.
8. Test all endpoints via Swagger UI, including JWT-protected ones.
9. Add descriptions for each serializer field for better docs.
10. Document nested serializers (enrollments inside students).

---

