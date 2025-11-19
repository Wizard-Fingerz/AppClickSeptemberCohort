# Django Templates in a School Portal — Comprehensive Note

---

## 1. Overview: What are Django Templates (in a School Portal)?

* Django templates are the presentation layer (View) in the MVT pattern, used to generate dynamic HTML for the school portal.
* Purpose: Keep the presentation of content (HTML for students, teachers, and admin) separate from backend logic.
* Templates use Django's template language (`{{ }}` and `{% %}`) for rendering variables (like student names, grades), logic, includes, and reusable components.

---

## 2. Basic Concepts & Syntax (School Portal Examples)

### Variables

```html
<p>Hello, {{ user.first_name }}!</p>
<p>Your current class: {{ student.current_class }}</p>
```

### Filters

```html
{{ announcement.title|upper }}
{{ student.grade|default:"Not Graded" }}
{{ result.score|floatformat:1 }}
```

### Tags (control flow, loops)

**View Example:**

```python
def dashboard(request):
    # Django injects 'user' into template context automatically
    return render(request, 'dashboard.html')
```

**Template (`dashboard.html`):**

```django
{% if user.is_authenticated %}
  <p>Welcome, {{ user.username }}!</p>
  <a href="{% url 'logout' %}">Logout</a>
{% else %}
  <a href="{% url 'login' %}">Login</a>
{% endif %}
```

**Loop Example (List of Students):**

```python
def class_list(request):
    students = Student.objects.filter(classroom__name="JSS1")
    return render(request, "students/class_list.html", {"students": students})
```

```django
<ul>
{% for student in students %}
  <li>{{ student.full_name }} ({{ student.registration_number }})</li>
{% empty %}
  <li>No students in this class.</li>
{% endfor %}
</ul>
```

*Include:*
```django
{% include "partials/navbar.html" %}
```

*Template inheritance:*
```django
{% extends "base.html" %}
{% block content %}
  <h1>Dashboard</h1>
{% endblock %}
```

---

## 3. Template Directory Setup (Typical School Portal)

* In `settings.py`, ensure `TEMPLATES` has the correct directories:
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
    },
]
```

* Folder structure example:
```
schoolportal/
├─ students/
│  └─ templates/students/...
├─ staff/
│  └─ templates/staff/...
├─ templates/
│  ├─ base.html
│  ├─ partials/
│  │  ├─ navbar.html
│  │  └─ footer.html
│  └─ dashboard.html
```

---

## 4. Template Inheritance

*Global layout in `base.html` (school portal style):*

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{% block title %}School Portal{% endblock %}</title>
  {% load static %}
  <link rel="stylesheet" href="{% static 'css/portal.css' %}">
  {% block head %}{% endblock %}
</head>
<body>
  {% include 'partials/navbar.html' %}
  <main>{% block content %}{% endblock %}</main>
  {% include 'partials/footer.html' %}
  {% block scripts %}{% endblock %}
</body>
</html>
```

*Example child template for student profile:*

```python
# views.py
def student_profile(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, "students/profile.html", {"student": student})
```

```django
{# templates/students/profile.html #}
{% extends "base.html" %}
{% block title %}{{ student.full_name }} — Profile{% endblock %}
{% block content %}
  <h1>{{ student.full_name }}</h1>
  <p>Registration No: {{ student.registration_number }}</p>
  <p>Class: {{ student.current_class }}</p>
{% endblock %}
```

---

## 5. Passing Data: Views → Templates

*Function-based view example (results sheet):*
```python
def result_sheet(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    results = Result.objects.filter(student=student)
    return render(request, 'students/result_sheet.html', {
        'student': student,
        'results': results
    })
```

*Class-based view for student details:*
```python
from django.views.generic import DetailView

class StudentDetailView(DetailView):
    model = Student
    template_name = "students/profile.html"
    context_object_name = "student"
```

---

## 6. Template Tags & Filters (Built-in, with School Portal Emphasis)

* Reverse URLs for attendance, results, etc: `{% url 'attendance_detail' record.pk %}`
* Static files (CSS, images): `{% load static %}` and then `{% static 'img/school_logo.png' %}`
* Using filters for presenting grades, scores with formatting:
  ```django
  {{ result.score|floatformat:1 }}
  ```
* Translate UI: `{% trans "Welcome" %}` (add i18n for multi-lingual schools if needed)

---

## 7. Custom Template Tags & Filters

*Use for repeated presentation logic (e.g., rendering student status, or calculating average score in templates).*

Example: `students/templatetags/school_tags.py`

```python
from django import template

register = template.Library()

@register.filter
def pass_fail(score):
    return "Passed" if score >= 50 else "Failed"
```

In template:
```django
{% load school_tags %}
{{ result.score|pass_fail }}
```

*Inclusion tag example (recent announcements partial):*

```python
@register.inclusion_tag('partials/recent_announcements.html')
def show_recent_announcements(count=4):
    from portal.models import Announcement
    announcements = Announcement.objects.order_by('-created_at')[:count]
    return {'announcements': announcements}
```
In template: `{% show_recent_announcements 4 %}`

---

## 8. Context Processors (School Info Example)

*Add site-wide variables to all templates, e.g., school name, session, overall stats.*

`portal/context_processors.py`
```python
def school_info(request):
    return {
        'SCHOOL_NAME': "Bright Future Academy",
        'CURRENT_SESSION': "2023/2024"
    }
```
Add in `settings.py`:
```python
'portal.context_processors.school_info',
```
Usage in template:
```django
{{ SCHOOL_NAME }} — Session: {{ CURRENT_SESSION }}
```

*Tip: Don’t run heavy database queries in context processors!*

---

## 9. Forms in Templates (e.g., Student Registration or Contact Form)

**Define a form in `forms.py`:**
```python
from django import forms
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name', 'registration_number', 'current_class', 'email']
```

**In view:**
```python
def register_student(request):
    form = StudentRegistrationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('student_success')
    return render(request, 'students/register.html', {'form': form})
```

**In template:**
```django
<form method="post" novalidate>
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Register</button>
</form>
```

**Field-by-field (for better control):**
```django
<label for="{{ form.current_class.id_for_label }}">Class</label>
{{ form.current_class }}
{% if form.current_class.errors %}
    <div class="errors">{{ form.current_class.errors }}</div>
{% endif %}
```

**Tip:** For beautiful forms, use [django-crispy-forms](https://django-crispy-forms.readthedocs.io):

- Install with `pip install django-crispy-forms crispy-bootstrap5`
- Add to `INSTALLED_APPS` and configure pack/settings.
- Use `{% load crispy_forms_tags %}` and render with `{{ form|crispy }}`

---

## 10. Static Files & Media

*Settings for your school’s brand assets, CSS, and user-uploaded files.*

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

*Templates:*
```django
{% load static %}
<link rel="stylesheet" href="{% static 'css/portal.css' %}">
<img src="{{ student.photo.url }}" alt="{{ student.full_name }}">
```

*Serve media in development:*
```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## 11. Pagination in Templates (E.g., Student Lists, Parent Lists)

*View:*
```python
from django.core.paginator import Paginator

def all_students(request):
    students = Student.objects.all()
    paginator = Paginator(students, 20)
    page = request.GET.get('page')
    students_page = paginator.get_page(page)
    return render(request, 'students/list.html', {'students': students_page})
```

*Template:*
```django
{% for s in students %}
  {{ s.full_name }}
{% endfor %}
<div class="pagination">
  {% if students.has_previous %}
    <a href="?page={{ students.previous_page_number }}">Prev</a>
  {% endif %}
  Page {{ students.number }} of {{ students.paginator.num_pages }}
  {% if students.has_next %}
    <a href="?page={{ students.next_page_number }}">Next</a>
  {% endif %}
</div>
```

---

## 12. Template Security & Escaping

* By default, Django escapes variables to prevent XSS. Always sanitize untrusted content before using `|safe`.
* Example: do **NOT** do `{{ request.POST.bio|safe }}` without cleaning input.
* For HTML from teachers' announcements/notes, sanitize server-side (e.g., with `bleach`).

**🔒 Key:** Always sanitize user content before marking as safe!  
See: [Django Output Escaping](https://docs.djangoproject.com/en/stable/topics/templates/#automatic-html-escaping)

---

## 13. Performance & Caching

* Use template fragment caching for slow-to-render blocks (e.g., stats summaries on dashboard):
```django
{% load cache %}
{% cache 600 dashboard_stats %}
  <!-- expensive template code -->
{% endcache %}
```
* Use `select_related` and `prefetch_related` in views for related objects (e.g. students and results).
* Do heavy computations in views, not in templates/context processors.

---

## 14. Internationalization (i18n)

* Mark strings for translation:
```django
{% load i18n %}
{% trans "Class" %}
```
* For variables:
```django
{% blocktrans %}Welcome, {{ student.full_name }}!{% endblocktrans %}
```

---

## 15. Testing Templates

* Use `django.test.Client` to test views/templates:
```python
from django.test import TestCase
from django.urls import reverse

class DashboardTemplateTest(TestCase):
    def test_dashboard_has_school_name(self):
        response = self.client.get(reverse('dashboard'))
        self.assertContains(response, "Bright Future Academy")
```
* Test custom template tags/filters in unit tests.

---

## 16. Advanced Patterns (for Large School Portals)

* Use includes/partials for navbar, student card, notifications, etc.
* Keep templates for each app under its own directory (`students/templates/students/`).
* Use static/ for unified CSS & JS across the portal.
* Keep main rendering server-side. Use JS sprinkles for things like attendance filtering with AJAX for teachers/admin.

---

## 17. Example: Student Profile Page — Templates Focus

### Models

```python
class Student(models.Model):
    full_name = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=20, unique=True)
    current_class = models.CharField(max_length=10)
    email = models.EmailField()
    photo = models.ImageField(upload_to='students/photos/', null=True, blank=True)
```

### View

```python
def student_profile(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/profile.html', {'student': student})
```

### Template

```django
{% extends "base.html" %}
{% block title %}{{ student.full_name }} — Profile{% endblock %}
{% block content %}
  <div class="student-profile">
    {% if student.photo %}
      <img src="{{ student.photo.url }}" alt="{{ student.full_name }}">
    {% endif %}
    <h1>{{ student.full_name }}</h1>
    <p>Reg#: {{ student.registration_number }}</p>
    <p>Class: {{ student.current_class }}</p>
    <p>Email: {{ student.email }}</p>
  </div>
{% endblock %}
```

---

## 18. Serving Templates & Static/Media in Production

* Run `python manage.py collectstatic` to gather static files.
* Use [whitenoise](http://whitenoise.evans.io/) or set up Nginx to serve static/media files.
* Keep `DEBUG = False` and properly set `ALLOWED_HOSTS` for school portal deployment.

---

## 19. Accessibility & Semantic HTML

* Use semantic tags and alt text:  
  `<img src="{{ student.photo.url }}" alt="{{ student.full_name }}">`
* Use clear headings, nav, landmark roles, and robust contrast per accessibility guidelines.
* Server-side rendering ensures screen readers and crawlers see all critical info.

---

## 20. Common School Portal Template Mistakes

* Expensive DB queries in templates/context processors (e.g., calculating class average in template — should be in view!).
* Not checking for missing images: `if student.photo`.
* Forgetting `{% csrf_token %}` in student/parent forms.
* Letting users submit rich text or HTML without server-side sanitization.

---

## 21. Debugging Template Issues

* Use `{{ variable|default:"(missing)" }}` to check context.
* With `DEBUG=True`, Django will show template errors and context tracebacks.
* Test template snippets interactively with `django.template.loader.render_to_string` in a shell.

---

## 22. Template-Related Performance Checklist

* Use `select_related`/`prefetch_related` on Student/Result Relations.
* Cache template blocks reused often.
* Avoid DB work inside custom tags/context processors.
* Use proper static asset versioning for CSS/JS (ManifestStaticFilesStorage).

---

## 23. Testing & CI

* Write tests for key student, result, and dashboard template views.
* Unit test custom template tags (e.g., pass/fail filter).
* Ensure static/media files are included in CI (test `collectstatic`).

---

## 24. Deployment & Production Tips

* Always set `DEBUG=False`.
* Set `ALLOWED_HOSTS`.
* Run `python manage.py collectstatic`.
* Use whitenoise or Nginx/CDN for static.
* Secure media storage (local, S3, or protected Nginx for report PDFs, etc).
* Secure headers and error monitoring.
* Enable fragment/full-page caching for slow dashboards.

---

## 25. Lesson Plan / Sequence (for a School Portal Project)

1. Intro to Django templates: Variables, filters, blocks (render student dashboard).
2. Template inheritance and includes: Build `base.html`, `navbar`, and a classroom child template.
3. Building forms (e.g. registration, result entry), error handling.
4. Working with static/media (school logo, student photos).
5. Loops, conditions, and adding pagination (e.g., student lists).
6. Create and test a custom template tag (pass/fail, class position).
7. Context processors (school info in nav).
8. Caching fragments (for school-wide stats).
9. Security: escaping, CSRF, and handling safe HTML.
10. Full school portal mini-project (profile, results, registration, dashboard).
11. Deploy static/media to production.

---

## 26. Assignments & Exercises

### Quick

* Loop over a class list and show “Passed” if a score ≥ 50.
* Make `base.html` and two child templates (dashboard, result list).

### Medium

* Build student list with pagination and an inclusion tag for recent announcements.
* Create registration form; render field errors below each input.

### Project (capstone)

* **School Portal mini-project:** student list, student detail/profile page, result entry form, dashboard summary. Use template inheritance, forms, context processor for school info, include partials for announcements. Add unit tests for two views and one custom template tag. Prepare a `README` showing how to set up static/media.

---

## 27. Cheatsheet — School Portal Template Shortcuts

* `{{ var|default:"-" }}` — fallback
* `{% url 'name' arg %}` — URL reverse
* `{% static 'path' %}` — file link
* `{% include 'file.html' %}` — partials
* `{% load static %}` — tag library
* `{% block name %}{% endblock %}` — child templates
* `{% csrf_token %}` — form protection

---

## 28. Further Resources for Students

* Django docs: [Templates](https://docs.djangoproject.com/en/stable/topics/templates/), [Forms](https://docs.djangoproject.com/en/stable/topics/forms/), [Static files](https://docs.djangoproject.com/en/stable/howto/static-files/)
* Django Debug Toolbar (performance/debugging)
* `django-crispy-forms` for great form HTML
* Whitenoise (easy static files in production)

---

## 29. Example: Minimal Files for Student Profile (complete)

`views.py`:

```python
from django.shortcuts import render, get_object_or_404
from .models import Student

def student_profile(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/profile.html', {'student': student})
```

`templates/students/profile.html`:

```django
{% extends "base.html" %}
{% block title %}{{ student.full_name }} - Profile{% endblock %}
{% block content %}
  <div class="student-profile">
    {% if student.photo %}
      <img src="{{ student.photo.url }}" alt="{{ student.full_name }}">
    {% endif %}
    <h1>{{ student.full_name }}</h1>
    <p>Registration No: {{ student.registration_number }}</p>
    <p>Class: {{ student.current_class }}</p>
    <p>Email: {{ student.email }}</p>
  </div>
{% endblock %}
```

---

## 30. Final Teaching Notes / Best Practices (for School Portal Templates)

* Keep templates clean: presentation-only. Do all calculations and queries in views/models.
* Use inheritance/includes for DRY code.
* Test and review template outputs.
* Avoid N+1 queries by using optimized queries and not looping relationships in templates.
* Escape user content unless you thoroughly sanitize.
* Use fragment caching for expensive dashboard/stats sections.
* Group templates by app: `templates/students/`, `templates/staff/`, etc. to prevent name collision and improve maintainability.

