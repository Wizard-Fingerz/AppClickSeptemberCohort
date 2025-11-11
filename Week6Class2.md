

# 🌐 **Django URLs — Routing Requests to Views**

---

## 🧠 **1. What is a URL in Django?**

In Django, a **URL** (Uniform Resource Locator) tells the framework which view should handle a specific web request.

When a user visits:

```
http://127.0.0.1:8000/students/
```

Django looks up a matching **URL pattern** in your project’s configuration and calls the corresponding **view**.

✅ **In short:**

> Django URLs act as “traffic controllers” — directing incoming requests to the correct view function or class.

---

## 🧩 **2. URL Configuration (URLconf)**

A **URLconf** is a Python module (`urls.py`) that maps **URL patterns** to **views**.

Django looks for URL patterns in two main places:

1. The **project-level** `urls.py` (main configuration)
2. The **app-level** `urls.py` (specific to each app)

---

## 📁 **3. The Default Project Structure**

When you create a new Django project (`django-admin startproject myproject`), it includes a file called `urls.py`.

Example:

```
myproject/
│
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py   ← main URL configuration
│   └── wsgi.py
│
└── students/
    ├── views.py
    ├── urls.py   ← app-level URL configuration
```

---

## ⚙️ **4. Example of Project-Level `urls.py`**

`myproject/urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path('students/', include('students.urls'))  # Include app’s URL file
]
```

✅ The `include()` function tells Django to **look inside another app’s URL file** (`students/urls.py`).

---

## 🧩 **5. App-Level `urls.py`**

Inside your app (e.g., `students`), create a file named `urls.py`:

```
students/
│
├── views.py
└── urls.py
```

`students/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('<int:id>/', views.student_detail, name='student_detail'),
]
```

✅ This setup allows:

* `/students/` → calls `student_list` view
* `/students/1/` → calls `student_detail` view

---

## 🧱 **6. URL Patterns and Path Converters**

`path()` is the most common way to define URLs.

**Syntax:**

```python
path('route/', view, name='name_of_url')
```

You can use **path converters** to capture parts of the URL.

| Converter        | Example                        | Description              |
| ---------------- | ------------------------------ | ------------------------ |
| `<int:id>`       | `/student/5/`                  | Integer parameter        |
| `<str:username>` | `/user/john/`                  | String parameter         |
| `<slug:slug>`    | `/blog/intro-to-python/`       | Slug (text-friendly URL) |
| `<uuid:id>`      | `/profile/550e8400-e29b-41d4/` | UUID parameter           |
| `<path:subpath>` | `/files/images/pic1.jpg`       | Captures entire path     |

### 🧪 Example

```python
urlpatterns = [
    path('student/<int:id>/', views.student_detail),
    path('user/<str:username>/', views.user_profile),
]
```

---

## 🧭 **7. Naming Your URLs**

Every path can have a **name**, which is extremely helpful for reverse URL lookups in templates and code.

Example:

```python
path('student/<int:id>/', views.student_detail, name='student_detail')
```

### Use in Template:

```html
<a href="{% url 'student_detail' id=1 %}">View Student</a>
```

✅ **Advantage:**
If you later change the actual URL pattern, the template still works — only the `urls.py` needs updating.

---

## 🧩 **8. Using `include()` for Modularity**

In large projects, you’ll have multiple apps.
`include()` lets you split URL patterns cleanly.

Example in main `urls.py`:

```python
urlpatterns = [
    path('students/', include('students.urls')),
    path('teachers/', include('teachers.urls')),
]
```

✅ Keeps your code modular and readable.

---

## 🧩 **9. Using `re_path()` for Regular Expressions**

If you need advanced matching, use `re_path()` (regex-based).

Example:

```python
from django.urls import re_path

urlpatterns = [
    re_path(r'^student/(?P<id>\d+)/$', views.student_detail),
]
```

✅ `(?P<id>\d+)` captures digits and sends them to the view as `id`.

---

## 🧰 **10. URL Reverse Resolution**

You can dynamically generate URLs in Python code using the `reverse()` function.

```python
from django.urls import reverse

url = reverse('student_detail', args=[3])
print(url)  # Output: '/students/3/'
```

---

## 🧠 **11. Serving Static and Media Files (During Development)**

When developing locally, you can configure static and media URLs in your `urls.py`.

Example:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

✅ This allows you to serve uploaded files and static assets in development mode.

---

## ⚙️ **12. Example: Full Project URL Flow**

**Request:**
`GET /students/5/`

**Django Process:**

1. `myproject/urls.py` — finds `'students/'` → includes `students.urls`
2. `students/urls.py` — matches `<int:id>/` → calls `views.student_detail`
3. `views.student_detail` — processes and returns HTML response

---

## 🧪 **13. Example Code Recap**

### `students/views.py`

```python
from django.shortcuts import render
from django.http import HttpResponse

def student_list(request):
    return HttpResponse("List of all students")

def student_detail(request, id):
    return HttpResponse(f"Details of student with ID {id}")
```

### `students/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('<int:id>/', views.student_detail, name='student_detail'),
]
```

### `myproject/urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
]
```

✅ Visit:

* `/students/` → “List of all students”
* `/students/1/` → “Details of student with ID 1”

---

## 🧠 **14. Best Practices**

✅ Use **`include()`** for modular URL organization.
✅ Always **name your URLs** (e.g., `name='student_detail'`).
✅ Use **path converters** instead of regex when possible (simpler).
✅ Use `reverse()` and `{% url %}` for dynamic linking.
✅ Keep **project URLs** clean — only include app routes.

---

## 🧪 **15. Exercises**

Try these to reinforce your understanding 👇

1. Create a `teachers` app with its own `urls.py`.
2. Add a `home` view at the root URL (`/`) using `TemplateView`.
3. Create a URL pattern that displays student names by slug (e.g., `/students/john-doe/`).
4. Add a view that redirects from `/students/latest/` to `/students/1/`.
5. Create a regex URL pattern using `re_path()` for IDs that only accept numbers.
6. Use `{% url %}` in a template to link between student and teacher pages.
7. Experiment with `reverse()` inside a view to print the URL of another view.

---

