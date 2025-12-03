
---

# ⭐ **ERROR HANDLING IN DJANGO (Comprehensive Guide)**

Error handling in Django ensures that your application does not crash when something goes wrong. Instead, Django gracefully catches the error and provides a controlled response.

---

# 🔵 1. **Django Default Error Handling**

### When `DEBUG = True`

Django shows detailed error pages including:

* Error type
* Line number
* Stack trace
* Environment info

This is ideal for development.

---

### When `DEBUG = False`

Django hides internal details for security and instead shows:

* A simple 404 page ("Not Found")
* A simple 500 page ("Server Error")

This is ideal for production.

---

# 🔵 2. **Python Try/Except in Django Views**

You can catch errors directly in views using `try/except`.

### Example:

```python
from django.http import HttpResponse

def divide(request):
    try:
        result = 10 / 0
        return HttpResponse(f"Result: {result}")
    except ZeroDivisionError:
        return HttpResponse("Error: Cannot divide by zero!")
```

---

### Multiple Exceptions

```python
try:
    user = User.objects.get(id=user_id)
except User.DoesNotExist:
    return HttpResponse("User not found")
except Exception as e:
    return HttpResponse(f"Unknown error: {e}")
```

---

# 🔵 3. **Error Handling with Django ORM**

### Example: Handling Object Not Found

```python
from django.http import Http404

def get_student(request, id):
    try:
        student = Student.objects.get(pk=id)
    except Student.DoesNotExist:
        raise Http404("Student does not exist")
    
    return render(request, "student.html", {"student": student})
```

This will render a default 404 page.

---

# 🔵 4. **Shortcuts for Error Handling**

### `get_object_or_404()`

A common shortcut used in Django:

```python
from django.shortcuts import get_object_or_404

student = get_object_or_404(Student, pk=id)
```

If the object does not exist → Django automatically returns a **404 page**.

---

### `get_list_or_404()`

```python
students = get_list_or_404(Student, grade="A")
```

---

# 🔵 5. **Handling Form Errors**

Django forms have built-in validation.

### In `forms.py`

```python
from django import forms

class RegisterForm(forms.Form):
    email = forms.EmailField()
    age = forms.IntegerField()

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise forms.ValidationError("You must be at least 18 years old.")
        return age
```

---

### In `views.py`

```python
def register(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        # process data
        pass
    else:
        print(form.errors)   # shows error messages
    
    return render(request, "register.html", {"form": form})
```

---

### In `template.html`

```html
{{ form.errors }}
```

Django automatically displays:

* Field-specific errors
* Required field errors
* ValidationError messages

---

# 🔵 6. **Custom Error Pages (404, 500, 403, 400)**

### Step 1: Turn off DEBUG

```python
DEBUG = False
ALLOWED_HOSTS = ['*']
```

---

### Step 2: Create error templates

### In `templates/404.html`

```html
<h1>Page Not Found</h1>
<p>The page you are looking for does not exist.</p>
```

### In `templates/500.html`

```html
<h1>Server Error</h1>
<p>Something went wrong on our side. Please try again later.</p>
```

### Optional:

* `403.html` → forbidden
* `400.html` → bad request

Django automatically uses these templates when errors occur.

---

# 🔵 7. **Raising Custom Errors**

### Raise a custom 403 error

```python
from django.core.exceptions import PermissionDenied

def dashboard(request):
    if not request.user.is_staff:
        raise PermissionDenied
    return render(request, "dashboard.html")
```

---

### Raise a custom 400 error

```python
from django.http import HttpResponseBadRequest

def example(request):
    return HttpResponseBadRequest("Invalid request format")
```

---

# 🔵 8. **Handling Errors in APIs (Django REST Framework)**

Example of DRF exception handler:

```python
from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        response.data['status_code'] = response.status_code

    return response
```

---

# 🔵 9. **Logging Errors in Django**

Logs help you track errors in production.

### In `settings.py`

```python
LOGGING = {
    'version': 1,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'errors.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
```

Now every error is stored in **errors.log**.

---

# 🔵 10. **Best Practices for Error Handling in Django**

✔ Use `try/except` sparingly — don't overuse
✔ Use `get_object_or_404()` instead of manual try
✔ Always create custom 404 and 500 pages
✔ Log your errors
✔ Never expose sensitive data in error messages
✔ Use form validation instead of manual checks
✔ Do NOT show debug info in production
✔ Use middleware for global error handling

---

# 🟢 **Exercises (10 Practical Tasks)**

1. Create a view that divides two numbers and handle ZeroDivisionError
2. Handle a missing user using `try/except`
3. Replace that with `get_object_or_404()`
4. Create a custom 404 page
5. Create a form and raise a validation error if username < 5 characters
6. Build a form that rejects emails not ending with `.com`
7. Raise a custom PermissionDenied if a user is not authenticated
8. Create a 500.html page and force an error to test it
9. Add logging and generate an error to see it saved
10. Build an API (DRF) and implement a custom exception_handler

---
