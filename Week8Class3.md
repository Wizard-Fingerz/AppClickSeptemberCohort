

---

# 🔄 **Django Loops & Iterations**

---

## 🧠 **1. Loops in Django Templates**

Django templates use the `{% for %}` tag to iterate over **lists, querysets, or any iterable object** passed from views.

---

### Basic Syntax

```html
{% for item in list %}
    {{ item }}
{% endfor %}
```

### Example — Simple List

**View (`views.py`)**

```python
from django.shortcuts import render

def student_list(request):
    students = ['John', 'Mary', 'Alex', 'Sophia']
    return render(request, 'students/list.html', {'students': students})
```

**Template (`list.html`)**

```html
<h2>Student List</h2>
<ul>
{% for student in students %}
    <li>{{ student }}</li>
{% endfor %}
</ul>
```

✅ Output:

```
- John
- Mary
- Alex
- Sophia
```

---

## 🧩 **2. Looping Through Querysets**

When you pass a **Django model queryset** to a template:

**View**

```python
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students})
```

**Template**

```html
<ul>
{% for student in students %}
    <li>{{ student.name }} - {{ student.grade }}</li>
{% empty %}
    <li>No students found.</li>
{% endfor %}
</ul>
```

✅ `{% empty %}` runs if the iterable is empty.

---

## 🧠 **3. Loop Variables**

Django provides **special loop variables**:

| Variable              | Description                        |
| --------------------- | ---------------------------------- |
| `forloop.counter`     | 1-based index                      |
| `forloop.counter0`    | 0-based index                      |
| `forloop.revcounter`  | Reverse counter (1-based)          |
| `forloop.revcounter0` | Reverse counter (0-based)          |
| `forloop.first`       | True if first iteration            |
| `forloop.last`        | True if last iteration             |
| `forloop.parentloop`  | Access parent loop in nested loops |

**Example**

```html
<ul>
{% for student in students %}
    <li>
        {{ forloop.counter }}. {{ student.name }} - {{ student.grade }}
        {% if forloop.first %}(First Student){% endif %}
        {% if forloop.last %}(Last Student){% endif %}
    </li>
{% endfor %}
</ul>
```

---

## 🧩 **4. Nested Loops**

You can loop over **nested lists or dictionaries**.

**Example — Students & Courses**

```python
students = [
    {'name': 'John', 'courses': ['Math', 'Physics']},
    {'name': 'Mary', 'courses': ['Biology', 'Chemistry']},
]
```

**Template**

```html
{% for student in students %}
    <h3>{{ student.name }}</h3>
    <ul>
        {% for course in student.courses %}
            <li>{{ course }}</li>
        {% endfor %}
    </ul>
{% endfor %}
```

---

## 🧩 **5. Looping Over Dictionaries**

If you pass a dictionary to the template:

```python
grades = {'John': 'A', 'Mary': 'B', 'Alex': 'C'}
return render(request, 'students/grades.html', {'grades': grades})
```

**Template**

```html
<ul>
{% for name, grade in grades.items %}
    <li>{{ name }} - {{ grade }}</li>
{% endfor %}
</ul>
```

---

## 🧠 **6. Combining Loops and Conditions**

Loops are often combined with **if conditions** to filter data:

```html
<ul>
{% for student in students %}
    {% if student.grade == 'A' %}
        <li>{{ student.name }} - {{ student.grade }}</li>
    {% endif %}
{% endfor %}
</ul>
```

✅ Only students with grade "A" will be displayed.

---

## 🧩 **7. Using `forloop` with CSS Classes**

You can apply **different styles** for first, last, or even/odd rows:

```html
<ul>
{% for student in students %}
    <li class="{% if forloop.first %}first{% elif forloop.counter0|divisibleby:2 %}even{% else %}odd{% endif %}">
        {{ student.name }} - {{ student.grade }}
    </li>
{% endfor %}
</ul>
```

* `divisibleby` filter checks if index is divisible by a number.

---

## 🧩 **8. Loop Filters**

* `|length` → Count the number of items
* `|slice` → Select a portion of the list
* `|dictsort` → Sort dictionary items

**Example**

```html
{% for student in students|slice:":3" %}
    <li>{{ student.name }}</li>
{% endfor %}
```

✅ Shows only the first 3 students.

---

## 🧰 **9. Exercises**

1. Display all students in an unordered list.
2. Highlight the **first student** with `(First)` using `forloop.first`.
3. Loop through a list of courses and display only courses that start with "M".
4. Display a **numbered list** using `forloop.counter`.
5. Loop through a nested dictionary of students and courses and display them.
6. Apply **alternate row colors** using `forloop.counter0|divisibleby:2`.
7. Display a **message** if the student list is empty using `{% empty %}`.
8. Sort a dictionary of student grades alphabetically and display them.
9. Combine loops and conditions to show only students with grade A or B.
10. Display the last student in the list with `(Last)` using `forloop.last`.

---

## ✅ **Summary**

| Feature                                          | Usage                                       |
| ------------------------------------------------ | ------------------------------------------- |
| `{% for item in list %} ... {% endfor %}`        | Basic loop                                  |
| `{% empty %}`                                    | Handle empty lists                          |
| `forloop.counter / forloop.first / forloop.last` | Loop metadata                               |
| Nested loops                                     | Loop through lists of lists or dictionaries |
| Combine with `{% if %}`                          | Conditional rendering inside loops          |
| Filters (`slice`, `dictsort`, `length`)          | Control loop output                         |

---


