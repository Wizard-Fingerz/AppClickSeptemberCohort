

---

# 📝 **Django Forms & CRUD Operations (Comprehensive Guide)**

---

## 🧠 **1. What is a Django Form?**

A **form** is a way to **accept input from users**.

In Django, forms can be:

1. **HTML forms manually created** — basic forms
2. **Django Form classes** — built-in Python classes that handle validation, widgets, and database integration.

Django forms make it easier to:

* Validate input
* Display errors
* Handle POST requests
* Connect with models automatically (ModelForms)

---

## ⚙️ **2. Two Types of Django Forms**

| Type                                   | Description                                            |
| -------------------------------------- | ------------------------------------------------------ |
| **Form (django.forms.Form)**           | Standard forms for general input                       |
| **ModelForm (django.forms.ModelForm)** | Automatically links to a database model and saves data |

---

## 🧩 **3. Creating a Simple Form**

`forms.py` in your app (`students/forms.py`):

```python
from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    grade = forms.CharField(max_length=10)
```

### View to handle form (`views.py`)

```python
from django.shortcuts import render
from .forms import StudentForm

def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # Access data
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            grade = form.cleaned_data['grade']
            # You can save to DB here manually
            return render(request, 'students/success.html', {'name': name})
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})
```

### Template (`student_form.html`)

```html
<h2>Add Student</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>
```

✅ `{{ form.as_p }}` renders the form fields with HTML `<p>` tags automatically.

---

## 🧩 **4. ModelForm — Forms Directly Linked to Models**

`forms.py`

```python
from django import forms
from .models import Student

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'grade', 'teacher']  # Fields to include
```

### View to handle ModelForm

```python
from django.shortcuts import render, redirect
from .forms import StudentModelForm

def add_student(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()  # Automatically saves to DB
            return redirect('student_list')
    else:
        form = StudentModelForm()
    return render(request, 'students/add_student.html', {'form': form})
```

✅ `form.save()` automatically creates a new **Student** record.

---

## 🧩 **5. CRUD Operations in Django**

CRUD = **Create, Read, Update, Delete**

### 5.1 **Create**

* Use a **ModelForm** to accept input
* `form.save()` stores it in the database
* Example: `add_student` view above

---

### 5.2 **Read**

* Fetch records using the **ORM**

```python
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})
```

**Template (`student_list.html`)**

```html
<h2>All Students</h2>
<ul>
{% for student in students %}
    <li>{{ student.name }} - {{ student.grade }} - <a href="{% url 'student_update' student.id %}">Edit</a> | <a href="{% url 'student_delete' student.id %}">Delete</a></li>
{% endfor %}
</ul>
```

---

### 5.3 **Update**

* Pre-fill form with existing data
* Save updates using `.save()`

**View (`views.py`)**

```python
from django.shortcuts import get_object_or_404

def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentModelForm(instance=student)
    return render(request, 'students/add_student.html', {'form': form})
```

✅ `instance=student` pre-fills form with existing data.

---

### 5.4 **Delete**

**View (`views.py`)**

```python
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'students/confirm_delete.html', {'student': student})
```

**Template (`confirm_delete.html`)**

```html
<h2>Are you sure you want to delete {{ student.name }}?</h2>
<form method="post">
    {% csrf_token %}
    <button type="submit">Yes, Delete</button>
    <a href="{% url 'student_list' %}">Cancel</a>
</form>
```

---

## 🧩 **6. URL Patterns for CRUD**

`urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('add/', views.add_student, name='student_add'),
    path('update/<int:id>/', views.update_student, name='student_update'),
    path('delete/<int:id>/', views.delete_student, name='student_delete'),
]
```

---

## 🧠 **7. Best Practices**

✅ Use **ModelForms** instead of manual forms whenever possible.
✅ Always use `get_object_or_404()` for update/delete views.
✅ Use **redirect()** after POST to prevent duplicate form submissions.
✅ Keep templates clean — logic belongs in **views or models**.
✅ Always use `{% csrf_token %}` in POST forms for security.

---

## 🧰 **8. Practical Exercises**

1. Create a full CRUD app for **Teachers**:

   * Add new teacher
   * List teachers
   * Update teacher info
   * Delete teacher
2. Create a CRUD app for **Courses** with many-to-many relation with students.
3. Add **form validation** to ensure age > 0.
4. Add **success messages** after create/update/delete.
5. Create a **search function** to filter students by name.
6. Pre-fill a form with **default values** for new students.
7. Add **pagination** to student list.
8. Create a **dashboard** page showing the count of students and teachers.
9. Make a **confirmation page** before deleting a course.
10. Use **inline formsets** to add multiple students under one teacher at once.

---

## 🧩 **9. Summary**

| Operation  | Method                         | Key Notes                                 |
| ---------- | ------------------------------ | ----------------------------------------- |
| **Create** | POST + ModelForm               | `form.save()` stores record               |
| **Read**   | GET + ORM                      | `Model.objects.all()` / `filter()`        |
| **Update** | POST + ModelForm(instance=...) | Pre-fill form, call `save()`              |
| **Delete** | POST                           | Use `get_object_or_404()` then `delete()` |

---

With **Forms & CRUD**, you can now build **fully interactive Django applications**.

---
