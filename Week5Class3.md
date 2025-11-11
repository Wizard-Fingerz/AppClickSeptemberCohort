

---

# 🧱 **Introduction to Django MVT Structure**

---

## 🧠 **1. What is the Django MVT Architecture?**

Django follows the **MVT Pattern**, which stands for:
👉 **Model – View – Template**

It’s **similar** to the popular **MVC (Model–View–Controller)** pattern used in other frameworks — but Django gives it its own twist.

| MVC Concept    | Django Equivalent       | Description                                           |
| -------------- | ----------------------- | ----------------------------------------------------- |
| **Model**      | Model                   | Defines your data (database tables and logic)         |
| **View**       | View                    | Contains the logic that connects models and templates |
| **Controller** | Django Framework itself | Handles routing, requests, and responses              |
| **Template**   | Template                | Defines the structure of what the user sees (HTML)    |

So, in Django:

> “**The framework is the controller.** Your job is to write the Model, View, and Template.”

---

## ⚙️ **2. The MVT Workflow**

Here’s how Django processes a request step-by-step 👇

1. **User** types a URL in the browser.
2. Django checks the **URLconf (urls.py)** for a matching route.
3. The matched URL calls a **View function** (views.py).
4. The view function:

   * Interacts with the **Model** (database),
   * Passes data to the **Template**.
5. The **Template** returns an HTML page as the **response** to the user.

---

### 🧩 Visual Flow:

```
User → URL → View → Model → Template → Response
```

---

## 📁 **3. Django MVT Folder Structure**

Let’s look at a simple app structure:

```
schoolportal/
├── manage.py
├── schoolportal/
│   ├── settings.py
│   ├── urls.py
│
└── students/
    ├── models.py        ← Model
    ├── views.py         ← View
    ├── templates/       ← Template folder
    │   └── students/
    │       └── home.html
    ├── urls.py
```

---

## 🧩 **4. The Model (Database Layer)**

The **Model** is the Python representation of your database table.
You define your data structure here.

### Example — `students/models.py`

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    grade = models.CharField(max_length=10)

    def __str__(self):
        return self.name
```

✅ **Explanation:**

* `models.Model` — base class for all models
* Each attribute (`name`, `age`, `grade`) represents a column in the database table
* Django automatically creates the table when you run migrations

### Apply it:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 🧩 **5. The View (Logic Layer)**

The **View** is a Python function or class that handles a web request and returns a web response.
It connects the model (data) with the template (presentation).

### Example — `students/views.py`

```python
from django.shortcuts import render
from .models import Student

def student_list(request):
    students = Student.objects.all()  # Fetch all students from database
    return render(request, 'students/student_list.html', {'students': students})
```

✅ **Explanation:**

* `Student.objects.all()` fetches all records
* `render()` combines data (`students`) with an HTML file (`student_list.html`)

---

## 🧩 **6. The Template (Presentation Layer)**

Templates are **HTML files** that display data to the user.

### Example — `students/templates/students/student_list.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Student List</title>
</head>
<body>
    <h1>All Students</h1>
    <ul>
        {% for student in students %}
            <li>{{ student.name }} - {{ student.grade }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

✅ **Explanation:**

* Django Template Language (DTL) uses `{% %}` for logic (loops, conditions)
* `{{ }}` for variables (dynamic data)

---

## 🔗 **7. URL Configuration**

To connect everything, we use **urls.py**.

### In `students/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
]
```

### In `schoolportal/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
]
```

✅ **Now the URL `/students/`** will trigger `student_list()` view and show the template.

---

## 🧠 **8. How Everything Connects**

| Component    | File         | Function                   |
| ------------ | ------------ | -------------------------- |
| **URL**      | `urls.py`    | Maps route to view         |
| **View**     | `views.py`   | Handles logic and data     |
| **Model**    | `models.py`  | Manages database structure |
| **Template** | `templates/` | Displays the data to user  |

---

### Example Flow:

When you visit →
🔗 `http://127.0.0.1:8000/students/`

Django does this:

1. Looks for `/students/` in `urls.py`
2. Finds and calls the `student_list` view
3. View fetches data from `Student` model
4. Sends data to `student_list.html`
5. Renders and returns it as a webpage

---

## 🧩 **9. Practical Mini Project: “Students Directory”**

**Goal:**
Display a list of students and allow adding new ones.

**Steps:**

1. Create the `Student` model (as above)
2. Create the view (`student_list`)
3. Create a template with a form to add a student
4. Add URLs for both list and add views
5. Use Django Admin to add data easily

---

## 🧰 **10. Summary of Key Points**

| Component    | Purpose                             | File          |
| ------------ | ----------------------------------- | ------------- |
| **Model**    | Handles database operations         | `models.py`   |
| **View**     | Business logic (fetch/process data) | `views.py`    |
| **Template** | User interface                      | `templates/`  |
| **URLConf**  | Route URLs to views                 | `urls.py`     |
| **Settings** | Global project configuration        | `settings.py` |

---

## 🧩 **11. Exercise**

1. Create an app named `teachers`
2. Define a model `Teacher(name, subject, experience)`
3. Create a view to display all teachers
4. Create a `teacher_list.html` template
5. Connect everything using `urls.py`
6. Run the server and view the page

---

