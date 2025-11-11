
---

# ⚙️ **Conditions in Django**

In Django, conditions are mostly handled in **two places**:

1. **Views (Python code)** → Control the logic before sending data to templates
2. **Templates (HTML + Django Template Language)** → Control how data is displayed

---

## 🧠 **1. Conditional Logic in Views**

In your **views.py**, you can use standard Python `if`, `elif`, and `else` statements.

### Example — Simple Condition

```python
from django.shortcuts import render

def student_status(request):
    student_score = 75
    if student_score >= 70:
        status = "Pass"
    else:
        status = "Fail"
    return render(request, 'students/status.html', {'status': status})
```

**Template (`status.html`)**

```html
<p>Student Status: {{ status }}</p>
```

✅ Output: `Student Status: Pass`

---

### Example — Passing Boolean Conditions

```python
def welcome(request):
    user_logged_in = True
    return render(request, 'students/welcome.html', {'logged_in': user_logged_in})
```

**Template (`welcome.html`)**

```html
{% if logged_in %}
    <h2>Welcome back, User!</h2>
{% else %}
    <h2>Please log in to continue.</h2>
{% endif %}
```

---

## 🧩 **2. Conditional Logic in Templates**

Django uses **Template Tags** for conditions.

### 2.1 **If Tag**

```html
{% if condition %}
    <!-- Content if true -->
{% endif %}
```

### 2.2 **If-Else**

```html
{% if user.is_authenticated %}
    <p>Hello, {{ user.username }}!</p>
{% else %}
    <p>Please log in.</p>
{% endif %}
```

### 2.3 **If-Elif-Else**

```html
{% if student.grade == 'A' %}
    <p>Excellent!</p>
{% elif student.grade == 'B' %}
    <p>Good!</p>
{% else %}
    <p>Keep Trying!</p>
{% endif %}
```

---

### 2.4 **Using Operators**

Django supports:

* Comparison: `==`, `!=`, `>`, `<`, `>=`, `<=`
* Logical: `and`, `or`, `not`
* Membership: `in`, `not in`

Example:

```html
{% if student.age >= 18 and student.grade == 'A' %}
    <p>Eligible for scholarship.</p>
{% endif %}

{% if 'John' in student.name %}
    <p>Student name contains John.</p>
{% endif %}
```

---

### 2.5 **Empty and None Checks**

```html
{% if students %}
    <ul>
    {% for student in students %}
        <li>{{ student.name }}</li>
    {% endfor %}
    </ul>
{% else %}
    <p>No students available.</p>
{% endif %}
```

✅ `{% if students %}` returns `False` if the list is empty.

---

### 2.6 **Using Boolean Filters**

Django allows boolean filters like `if not`:

```html
{% if not user.is_staff %}
    <p>You do not have admin access.</p>
{% endif %}
```

---

## 🧩 **3. Conditional Logic in URLs (Optional)**

You can also conditionally redirect users in **views**:

```python
from django.shortcuts import redirect

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'students/dashboard.html')
    else:
        return redirect('login')
```

✅ Only authenticated users can see the dashboard.

---

## 🧠 **4. Best Practices**

1. Keep templates **mostly display logic** — heavy processing should be in **views**.
2. Avoid complex Python code in templates. Use **filters, tags, and context variables**.
3. Use `get_object_or_404` in views to avoid null errors.
4. Combine `{% if %}` with `{% for %}` to handle lists and conditions together.

---

## 🧰 **5. Exercises**

1. In a template, show “Good Job” if grade is A, “Keep Trying” otherwise.
2. Display “No students” if the student list is empty.
3. Show a “Login” button if user is not authenticated, “Logout” if logged in.
4. Display a message only if student.age > 18.
5. Loop through students and highlight those with grade B or above.
6. Redirect users in a view if they are not staff.
7. Use `{% if not %}` to hide content from non-admin users.

---

✅ **Summary:**

| Place         | Syntax                                                   | Use Case                                    |
| ------------- | -------------------------------------------------------- | ------------------------------------------- |
| **Views**     | Standard Python `if/elif/else`                           | Process data before sending to templates    |
| **Templates** | `{% if %} ... {% elif %} ... {% else %} ... {% endif %}` | Control what the user sees based on context |
| **Redirects** | `if condition: return redirect('url')`                   | Control navigation based on conditions      |

---

