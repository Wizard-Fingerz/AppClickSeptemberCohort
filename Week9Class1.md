
---

# 📘 **Django QuerySets (Comprehensive Guide)**

A **QuerySet** in Django represents a **collection of objects retrieved from the database**.

Example:

```python
students = Student.objects.all()
```

This returns a **QuerySet** of all Student records in the database.

---

# 🧠 **1. What is a QuerySet?**

A **QuerySet** is:

* Lazy (doesn’t hit the database until evaluated)
* Iterable (like a list)
* Chainable (you can apply multiple filters)
* Efficient (optimized SQL generation)

---

# 🧩 **2. Getting Data Using QuerySets**

### **2.1 `all()` – Get all records**

```python
students = Student.objects.all()
```

### **2.2 `get()` – Get a single object**

Returns exactly **one** object.

```python
student = Student.objects.get(id=1)
```

❗ **Raises error if**:

* Not found → `DoesNotExist`
* More than one result → `MultipleObjectsReturned`

### **2.3 `filter()` – Filter by condition**

Returns a **QuerySet** (zero or many results):

```python
passed_students = Student.objects.filter(score__gte=50)
```

### **2.4 `exclude()` – Opposite of filter**

```python
failed_students = Student.objects.exclude(score__gte=50)
```

---

# 🧠 **3. QuerySet Lookups**

Django uses **field lookups** to filter data.

| Lookup                     | Meaning                | Example                 |
| -------------------------- | ---------------------- | ----------------------- |
| `__exact`                  | exact match            | `name__exact='John'`    |
| `__iexact`                 | case-insensitive exact | `'john'`                |
| `__contains`               | substring              | `name__contains='jo'`   |
| `__icontains`              | case-insensitive       |                         |
| `__gte`                    | greater or equal       | `age__gte=18`           |
| `__lte`                    | less or equal          |                         |
| `__lt`, `__gt`             | less/greater than      |                         |
| `__startswith`, `endswith` | string operations      |                         |
| `__in`                     | list of values         | `id__in=[1,2,3]`        |
| `__range`                  | numeric range          | `score__range=(50, 80)` |
| `__year`, `__date`         | date lookup            | `created_at__year=2024` |

Example:

```python
students = Student.objects.filter(name__icontains="john", age__gte=18)
```

---

# 🔗 **4. Chaining QuerySets**

QuerySets can be chained because they return new QuerySets:

```python
students = Student.objects.filter(is_active=True).filter(age__gte=18)
```

---

# 🧲 **5. Ordering Results**

### **Ascending:**

```python
students = Student.objects.all().order_by('name')
```

### **Descending:**

```python
students = Student.objects.all().order_by('-name')
```

### **Multiple fields:**

```python
students = Student.objects.all().order_by('class_level', '-score')
```

---

# 🎯 **6. Limiting and Slicing QuerySets**

### Get first 10 records:

```python
students = Student.objects.all()[:10]
```

### Skipping:

```python
students = Student.objects.all()[10:20]
```

### First object:

```python
student = Student.objects.first()
```

### Last object:

```python
student = Student.objects.last()
```

---

# 🔍 **7. Checking Existence**

### Check if any record exists:

```python
Student.objects.filter(age=20).exists()
```

---

# 🧮 **8. Aggregation & Annotation**

Django provides aggregate functions:

### **Example aggregations**

```python
from django.db.models import Avg, Max, Min, Count, Sum

Student.objects.all().aggregate(Avg('score'))
```

### Output:

```python
{'score__avg': 72.4}
```

### Counting:

```python
Student.objects.count()
```

---

# 💡 **9. Using `values()` and `values_list()`**

### **`values()` returns dictionaries**

```python
Student.objects.values('name', 'score')
```

### **`values_list()` returns tuples**

```python
Student.objects.values_list('name', 'score')
```

### Get a flat list:

```python
Student.objects.values_list('name', flat=True)
```

---

# 🔄 **10. Bulk Operations**

### Create multiple objects:

```python
Student.objects.bulk_create([
    Student(name="John", score=80),
    Student(name="Ade", score=95),
])
```

### Update multiple rows:

```python
Student.objects.filter(class_level='SS2').update(score=70)
```

---

# 🔗 **11. Related Model QuerySets (Foreign Keys)**

Assume:

```python
class Teacher(models.Model):
    name = models.CharField(max_length=50)

class Student(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
```

### Get all students under a teacher:

```python
teacher = Teacher.objects.get(id=1)
teacher.student_set.all()
```

### Query students by teacher:

```python
Student.objects.filter(teacher__name="Mr. John")
```

---

# 🧠 **12. Q Objects (OR, AND, NOT Queries)**

Needed for **complex conditions**.

Example:

```python
from django.db.models import Q

students = Student.objects.filter(
    Q(score__gte=80) | Q(class_level='SS3')
)
```

NOT:

```python
Student.objects.filter(~Q(class_level='SS1'))
```

---

# 🚀 **13. F Expressions (Compare Two Fields)**

Compare field values without fetching:

```python
from django.db.models import F

Student.objects.filter(score__gt=F('previous_score'))
```

Add values:

```python
Student.objects.update(score=F('score') + 10)
```

---

# 🛠️ **14. QuerySet Evaluation**

A QuerySet is evaluated when:

* Iterated over
* Converted to list
* Sliced
* Used in booleans
* Accessed in template
* Used in `len()`

Example:

```python
list(Student.objects.all())
```

---

# 🧪 **15. Practical Examples**

### Get top 5 students:

```python
Student.objects.all().order_by('-score')[:5]
```

### Students who don’t have email:

```python
Student.objects.filter(email__isnull=True)
```

### Students created today:

```python
from django.utils.timezone import now

today = now().date()
Student.objects.filter(created_at__date=today)
```

---

# 🧰 **16. Exercises (20 Tasks)**

1. Get all records from a model.
2. Filter students whose age is greater than 18.
3. Get a student using `.get()`.
4. Use `icontains` to search for a name.
5. Sort students by name.
6. Get the last 3 created items.
7. Count total students.
8. Get students with score between 50 and 80.
9. Retrieve only name and score using `values()`.
10. Get a flat list of all student names.
11. Use Q to filter score > 70 OR class_level = "SS3".
12. Use annotation to compute average score.
13. Display top 10 highest-scoring students.
14. Exclude students with score below 20.
15. Use F expression to increase score by 5.
16. Filter records created this year.
17. Use `distinct()` on a field.
18. Filter students whose teacher is “Mr. Ade”.
19. Get a teacher and list all their students.
20. Use slicing to get every alternate student (`students[::2]`).

---

# ✅ **Conclusion**

Django QuerySets are:

* Powerful
* Flexible
* SQL-optimized
* Used everywhere in Django (views, forms, admin, templates)

Mastering QuerySets makes you strong in **backend development, data handling, and Django ORM**.

---
