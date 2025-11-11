

---

# 🔐 **Django Authentication — Comprehensive Guide**

---

## 🧠 **1. What is Django Authentication?**

Django comes with a **built-in authentication system** that handles:

* **User accounts** (registration, profiles)
* **Login and logout**
* **Permissions and access control**
* **Groups and user roles**

The main class is:

```python
from django.contrib.auth.models import User
```

Each `User` has:

| Attribute      | Purpose           |
| -------------- | ----------------- |
| `username`     | Unique identifier |
| `email`        | Email address     |
| `password`     | Hashed password   |
| `first_name`   | First name        |
| `last_name`    | Last name         |
| `is_staff`     | Admin access      |
| `is_superuser` | Full privileges   |
| `is_active`    | Active account    |
| `date_joined`  | Registration date |

---

## ⚙️ **2. Setting Up Authentication in Django**

Django’s **auth app** is enabled by default (`django.contrib.auth` in `INSTALLED_APPS`).
You also need:

```python
MIDDLEWARE = [
    ...,
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
]
```

✅ This enables session-based authentication.

---

## 🧩 **3. User Registration**

You can use Django’s built-in `UserCreationForm` for registration.

`forms.py`:

```python
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
```

`views.py`:

```python
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in after registration
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})
```

`urls.py`:

```python
path('register/', views.register, name='register')
```

`register.html`:

```html
<h2>Sign Up</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Register</button>
</form>
```

---

## 🧩 **4. User Login**

Use Django’s built-in `AuthenticationForm`.

`views.py`:

```python
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})
```

`login.html`:

```html
<h2>Login</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Login</button>
</form>
```

---

## 🧩 **5. User Logout**

`views.py`:

```python
from django.contrib.auth import logout

def user_logout(request):
    logout(request)
    return redirect('home')
```

`urls.py`:

```python
path('logout/', views.user_logout, name='logout')
```

✅ This ends the session and logs out the user.

---

## 🧩 **6. Restricting Access with Decorators**

Django provides **decorators** to restrict views:

### 6.1 `login_required`

```python
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html')
```

✅ Users not logged in are redirected to `login` page.

### 6.2 `user_passes_test`

```python
from django.contrib.auth.decorators import user_passes_test

def is_teacher(user):
    return user.groups.filter(name='Teachers').exists()

@user_passes_test(is_teacher)
def teacher_portal(request):
    ...
```

---

## 🧩 **7. Groups and Permissions**

Django allows creating **groups** with specific permissions.

### 7.1 Creating Groups

```python
from django.contrib.auth.models import Group, Permission

# Create a group
teachers_group, created = Group.objects.get_or_create(name='Teachers')

# Add permissions
permission = Permission.objects.get(codename='add_student')
teachers_group.permissions.add(permission)
```

### 7.2 Assign Users to Groups

```python
user.groups.add(teachers_group)
```

### 7.3 Check Permissions in Views

```python
if request.user.has_perm('students.add_student'):
    ...
```

---

## 🧩 **8. Password Management**

* **Change Password (while logged in)**

```python
from django.contrib.auth.forms import PasswordChangeForm
```

* **Reset Password (via email)**

```python
from django.contrib.auth.forms import PasswordResetForm
```

* **Django handles hashing** automatically — never store plaintext passwords.

---

## 🧩 **9. Example: Complete Authentication Flow**

### `urls.py`

```python
path('register/', views.register, name='register'),
path('login/', views.user_login, name='login'),
path('logout/', views.user_logout, name='logout'),
path('dashboard/', views.dashboard, name='dashboard'),
```

### `views.py`

```python
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

def register(request):
    form = SignUpForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('dashboard')
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('dashboard')
    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
```

✅ Now you have **registration, login, logout, and protected dashboard** fully working.

---

## 🧠 **10. Best Practices**

✅ Use Django’s **built-in authentication** instead of rolling your own.
✅ Always use `login_required` for sensitive pages.
✅ Use `UserCreationForm` and `AuthenticationForm` for reliability.
✅ Store passwords securely — Django hashes them automatically.
✅ Assign users to **groups** and use permissions for fine-grained control.
✅ Redirect after login/logout to improve UX.

---

## 🧰 **11. Exercises**

1. Create a **Teacher portal** that only logged-in teachers can access.
2. Add **registration** for students with email verification (simulate email).
3. Create a **profile page** that only the logged-in user can see.
4. Restrict editing student data to users with `add_student` permission.
5. Create a **group “Admins”** who can access the admin panel.
6. Implement a **change password page** for logged-in users.
7. Add a **logout button** in your base template visible only to logged-in users.
8. Display **user’s username** in the header when logged in.
9. Test **unauthorized access** to restricted pages.
10. Create a **password reset flow** using Django forms.

---

With this, you now have a **full foundation for building secure Django applications** with:

* User registration
* Login/logout
* Protected pages
* Groups and permissions

---

