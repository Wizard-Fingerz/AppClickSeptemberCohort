
---

# 🏗️ **Django Models — Comprehensive Guide**

---

## 🧠 **1. What is a Django Model?**

A **model** is a Python class that represents a **database table**.

Each attribute of the class corresponds to a **column** in the table, and each instance of the class corresponds to a **row** in the table.

### MVT Context:

```
Model → Handles all database operations
View → Fetches data from Model
Template → Displays data to user
```

---

## ⚙️ **2. Basic Model Structure**

**Example — `students/models.py`**

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    grade = models.CharField(max_length=10)

    def __str__(self):
        return self.name
```

### Explanation:

| Attribute   | Type                        | Purpose                                       |
| ----------- | --------------------------- | --------------------------------------------- |
| `name`      | `CharField(max_length=100)` | Text field, max length 100                    |
| `age`       | `IntegerField()`            | Integer field                                 |
| `grade`     | `CharField(max_length=10)`  | Text field for grade                          |
| `__str__()` | Method                      | Displays a human-readable name for the object |

---

## 🧩 **3. Common Field Types**

| Field Type      | Description      | Example                                             |
| --------------- | ---------------- | --------------------------------------------------- |
| `CharField`     | Short text       | `name = models.CharField(max_length=100)`           |
| `TextField`     | Long text        | `description = models.TextField()`                  |
| `IntegerField`  | Integer          | `age = models.IntegerField()`                       |
| `FloatField`    | Decimal numbers  | `price = models.FloatField()`                       |
| `BooleanField`  | True/False       | `is_active = models.BooleanField(default=True)`     |
| `DateField`     | Date only        | `dob = models.DateField()`                          |
| `DateTimeField` | Date & time      | `created = models.DateTimeField(auto_now_add=True)` |
| `EmailField`    | Email validation | `email = models.EmailField()`                       |
| `URLField`      | URL validation   | `website = models.URLField()`                       |
| `ImageField`    | Image upload     | `photo = models.ImageField(upload_to='photos/')`    |
| `FileField`     | File upload      | `resume = models.FileField(upload_to='files/')`     |

---

## ⚙️ **4. Field Options**

You can customize fields using parameters:

| Option              | Purpose                                        |
| ------------------- | ---------------------------------------------- |
| `max_length`        | Maximum length of text fields                  |
| `default`           | Default value if none is provided              |
| `blank=True`        | Field can be empty in forms                    |
| `null=True`         | Field can store NULL in the database           |
| `choices`           | Restrict field to a set of values              |
| `unique=True`       | Ensure uniqueness in the database              |
| `auto_now_add=True` | Automatically set current datetime on creation |
| `auto_now=True`     | Automatically update datetime on save          |

### Example with Options:

```python
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=50, choices=[('Math', 'Math'), ('Eng', 'English')])
    email = models.EmailField(unique=True)
    joined = models.DateTimeField(auto_now_add=True)
```

---

## 🧩 **5. Model Relationships**

Django supports **relationships** between models:

| Relationship      | Description               | Example                                                          |
| ----------------- | ------------------------- | ---------------------------------------------------------------- |
| `OneToOneField`   | One-to-one relationship   | `profile = models.OneToOneField(User, on_delete=models.CASCADE)` |
| `ForeignKey`      | Many-to-one relationship  | `teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)` |
| `ManyToManyField` | Many-to-many relationship | `courses = models.ManyToManyField(Course)`                       |

### Example — Students & Teachers

```python
class Teacher(models.Model):
    name = models.CharField(max_length=100)

class Student(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
```

✅ `on_delete=models.CASCADE` → deletes all students if the teacher is deleted.

---

## ⚙️ **6. Create & Apply Migrations**

After defining models, Django needs to create database tables.

### Step 1 — Make Migrations

```bash
python manage.py makemigrations
```

Output:

```
Migrations for 'students':
  students/migrations/0001_initial.py
```

### Step 2 — Apply Migrations

```bash
python manage.py migrate
```

✅ This creates the database tables.

---

## 🧩 **7. Django Admin Integration**

To manage models via the **admin interface**:

`students/admin.py`

```python
from django.contrib import admin
from .models import Student, Teacher

admin.site.register(Student)
admin.site.register(Teacher)
```

### Create Superuser

```bash
python manage.py createsuperuser
```

Visit:
`http://127.0.0.1:8000/admin/`
You can now add, edit, and delete records.

---

## 🧠 **8. Querying the Database (Django ORM)**

Django uses an **Object-Relational Mapper (ORM)** — you work with **Python objects** instead of SQL.

### Common Queries:

```python
from students.models import Student, Teacher

# Create
teacher = Teacher.objects.create(name='Mrs. Smith')
student = Student.objects.create(name='John Doe', teacher=teacher)

# Retrieve all
all_students = Student.objects.all()

# Retrieve single object
john = Student.objects.get(name='John Doe')

# Filter
students_a = Student.objects.filter(teacher__name='Mrs. Smith')

# Exclude
students_not_smith = Student.objects.exclude(teacher__name='Mrs. Smith')

# Order
students_ordered = Student.objects.all().order_by('name')

# Update
john.name = 'John D.'
john.save()

# Delete
john.delete()
```

---

## 🧩 **9. Advanced ORM Features**

### 9.1 Field Lookups

```python
Student.objects.filter(name__startswith='J')       # Starts with J
Student.objects.filter(age__gte=18)               # Age >= 18
Student.objects.filter(teacher__name__contains='Smith') # Teacher name contains
```

### 9.2 Aggregation

```python
from django.db.models import Count, Avg, Max, Min

avg_age = Student.objects.aggregate(Avg('age'))
```

### 9.3 Related Objects

```python
teacher = Teacher.objects.get(name='Mrs. Smith')
students = teacher.student_set.all()  # All students for this teacher
```

---

## ⚙️ **10. Model Meta Options**

`Meta` class defines **model behavior**:

```python
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        ordering = ['name']           # Default order
        verbose_name = 'Student Info' # Admin display
```

---

## 🧩 **11. Example: Complete Models**

```python
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    grade = models.CharField(max_length=10)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    enrolled_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
```

---

## 🧠 **12. Best Practices**

✅ Keep models simple — complex logic belongs in **views or managers**
✅ Use **verbose names** for clarity in admin
✅ Always use `__str__()` for readable object representation
✅ Use relationships properly (`ForeignKey`, `ManyToManyField`)
✅ Apply migrations immediately after changing models

---

## 🧰 **13. Exercises**

1. Create a `Course` model with `title`, `description`, and `credits`.
2. Create a many-to-many relationship between `Student` and `Course`.
3. Add a `Profile` model linked one-to-one with Django’s `User` model.
4. Write a query to get all students in grade “A”.
5. Filter students taught by a specific teacher.
6. Order students by age descending.
7. Count the total number of students.
8. Aggregate the average age of students.
9. Delete all students older than 25.
10. Create a custom manager that filters active students only.

---

## 📝 **14. Summary**

| Concept           | Purpose                                                            |
| ----------------- | ------------------------------------------------------------------ |
| **Model**         | Defines database tables and fields                                 |
| **Field Types**   | CharField, IntegerField, DateField, etc.                           |
| **Relationships** | OneToOne, ForeignKey, ManyToMany                                   |
| **Meta Options**  | Ordering, verbose_name, etc.                                       |
| **Migrations**    | `makemigrations` → create migration files; `migrate` → apply to DB |
| **Django ORM**    | Python interface for querying and manipulating data                |

---
