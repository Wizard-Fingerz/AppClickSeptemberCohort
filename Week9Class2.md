

---

# 🚀 **Advanced QuerySets in Django: `select_related` & `prefetch_related`**

When working with related models in Django (ForeignKey, OneToOne, ManyToMany, Reverse Relationships), Django ORM may generate **many hidden queries**.

Example of bad performance:

```python
students = Student.objects.all()
for student in students:
    print(student.teacher.name)
```

This may generate **N+1 queries**:

* 1 query to fetch students
* N queries (one for each student) to fetch teacher

To solve this, Django provides:

✔ **`select_related`** (JOIN)
✔ **`prefetch_related`** (two queries + Python merge)

---

# 🧠 **1. `select_related` — Uses SQL JOIN (Fastest for 1-to-1 or ForeignKey)**

### Use when:

* Relationship is **one-to-one** or **foreign key**
* You are accessing **one related object**

### Example Models:

```python
class Teacher(models.Model):
    name = models.CharField(max_length=50)

class Student(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
```

### Without select_related

```python
students = Student.objects.all()
for s in students:
    print(s.teacher.name)
```

This causes **N+1 queries**.

### With select_related

```python
students = Student.objects.select_related('teacher')
for s in students:
    print(s.teacher.name)
```

✔ **Only 1 query is made**
✔ Django performs an SQL JOIN to fetch student + teacher data in one query.

---

# 🔗 Allowed Relations for `select_related`

You can follow multiple relationships:

```python
Course.objects.select_related('teacher__department')
```

✔ Works with

* `ForeignKey`
* `OneToOneField`

❌ Does NOT work with:

* `ManyToManyField`
* reverse foreign keys

---

# 🧩 **2. `prefetch_related` — For Many-to-Many and Reverse FK**

Use when:

* Relationship returns **multiple objects**
* ManyToMany
* Reverse ForeignKey (e.g., teacher → students)

### Example Model

```python
class Student(models.Model):
    name = models.CharField(max_length=50)
    courses = models.ManyToManyField('Course')

class Course(models.Model):
    title = models.CharField(max_length=100)
```

### Without prefetch_related

```python
students = Student.objects.all()
for s in students:
    for c in s.courses.all():
        print(c.title)
```

Bad: This triggers **lots of queries**.

### With prefetch_related

```python
students = Student.objects.prefetch_related('courses')
for s in students:
    for c in s.courses.all():
        print(c.title)
```

How it works:

* Query 1 → All students
* Query 2 → All student-course relationships
* Django joins them in Python memory

✔ **2 queries only, regardless of size**
✔ Best for *many-to-many* and *reverse relations*
✔ Does not use SQL JOIN

---

# 📊 **3. select_related vs prefetch_related (Comparison)**

| Feature       | select_related                | prefetch_related                 |
| ------------- | ----------------------------- | -------------------------------- |
| Type          | SQL JOIN                      | Two queries + Python merge       |
| Suitable For  | FK & OneToOne                 | ManyToMany & reverse FK          |
| Performance   | Faster for single related row | Best for multiple rows           |
| Database Load | More (big joined rows)        | Less (separate queries)          |
| Data Size     | Can be heavy                  | Avoids duplication of large rows |

---

# 🧠 **4. Reverse Relationships with prefetch_related**

Model:

```python
class Teacher(models.Model):
    name = models.CharField(max_length=50)

class Student(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
```

To load all students for each teacher:

```python
teachers = Teacher.objects.prefetch_related('student_set')
```

Now:

```python
for t in teachers:
    print(t.name, t.student_set.all())
```

Only **2 queries**:

* Teachers
* Students

---

# 🧠 **5. Combining select_related + prefetch_related**

Example:

```python
blogs = Blog.objects.select_related('author').prefetch_related('comments')
```

* `author` → OneToOne → uses JOIN
* `comments` → ManyToMany or reverse FK → uses prefetch

✔ Most real apps use this combination.

---

# ⚙️ **6. Custom Prefetch Objects (Advanced)**

You can control the queryset that is prefetched.

Example:

```python
from django.db.models import Prefetch

students = Student.objects.prefetch_related(
    Prefetch('courses', queryset=Course.objects.filter(active=True))
)
```

So only active courses are prefetched.

---

# 🛠️ **7. Performance Tips**

1. **Use select_related for single-object joins**
2. **Use prefetch_related for multi-object joins**
3. Avoid huge `select_related` chains — too much JOIN slows performance
4. Use `Prefetch` to filter related data
5. Use Django Debug Toolbar to monitor queries

---

# 🧪 **8. Practical Examples**

### 8.1 Load posts with authors and comments

```python
Post.objects.select_related('author').prefetch_related('comments')
```

### 8.2 Load products with categories (ManyToMany)

```python
Product.objects.prefetch_related('categories')
```

### 8.3 Nested Prefetch

```python
Teacher.objects.prefetch_related('student_set__courses')
```

### 8.4 Double Optimization

```python
Order.objects.select_related('customer').prefetch_related('items')
```

---

# 🎯 **9. Exercises (15 Practical Tasks)**

1. Use `select_related` to load students with their teacher in one query.
2. Use `select_related` to load a blog post with its author.
3. Use `prefetch_related` to load all students with their courses.
4. Use `prefetch_related` to load teachers with all students.
5. Prefetch only active courses for students (use `Prefetch`).
6. Chain `select_related('teacher__department')` in a query.
7. Load all comments with each blog using `prefetch_related`.
8. Compare number of queries with and without `select_related`.
9. Compare number of queries with and without `prefetch_related`.
10. Use both: load books with authors + categories.
11. Optimize queryset for Order → customer + items.
12. Use prefetch on reverse relationship: categories → products.
13. Prefetch with filtering: load only "approved" comments.
14. Load all teams with players, and players with stats (nested prefetch).
15. Combine select + prefetch in a single query and explain why.

---

# ✅ **Conclusion**

`select_related` and `prefetch_related` are essential for **database optimization** in Django:

* `select_related` → Best for **single-object** relations (FK, OneToOne)
* `prefetch_related` → Best for **multi-object** relations (ManyToMany, reverse FK)
* Combine both for maximum efficiency

Mastering these makes your Django apps **fast, scalable, and production-ready**.

---
