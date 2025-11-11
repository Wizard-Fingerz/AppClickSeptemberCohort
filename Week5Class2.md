Perfect 👌 — now that you understand **how to install Django and set up a virtual environment**, the next step is to **create a Django project and app**, then learn how they work together.

Let’s go through it **comprehensively, step-by-step** so you’ll not only know the commands but also understand the **why** behind each step.

---

# 🏗️ **Creating a Django Project and App**

---

## 🧠 **1. Understanding Django’s Structure**

Before we start, it’s important to know two key concepts:

| Term        | Description                                                                                                           |
| ----------- | --------------------------------------------------------------------------------------------------------------------- |
| **Project** | The **overall website** — it contains configuration settings, URLs, database connections, etc.                        |
| **App**     | A **component** or **module** of your project (e.g., blog, user, chat, store). Each app performs a specific function. |

✅ Example:
A project = “School Portal”
Apps = “Students”, “Teachers”, “Results”, “Payments”, etc.

---

## ⚙️ **2. Create a Virtual Environment (If not already done)**

```bash
python -m venv venv
```

Activate it:

* On **Windows**:

  ```bash
  venv\Scripts\activate
  ```
* On **Mac/Linux**:

  ```bash
  source venv/bin/activate
  ```

---

## 📦 **3. Install Django**

```bash
pip install django
```

Verify:

```bash
django-admin --version
```

✅ Example output:

```
5.1
```

---

## 🏗️ **4. Create a Django Project**

Now create your main project directory:

```bash
django-admin startproject schoolportal
```

This will create a new folder like this:

```
schoolportal/
    manage.py
    schoolportal/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

---

## 🧾 **5. Understanding the Project Structure**

| File/Folder           | Description                                            |
| --------------------- | ------------------------------------------------------ |
| **manage.py**         | Command-line tool to run the server, create apps, etc. |
| **schoolportal/**     | The main project package                               |
| **settings.py**       | Contains configuration (database, apps, etc.)          |
| **urls.py**           | Routes URLs to views                                   |
| **asgi.py / wsgi.py** | Used for deployment (ASGI for async, WSGI for sync)    |
| **__init__.py**       | Marks the folder as a Python package                   |

---

## ⚡ **6. Run the Project**

Navigate into the project folder and start the development server:

```bash
cd schoolportal
python manage.py runserver
```

✅ Output:

```
Starting development server at http://127.0.0.1:8000/
```

Open your browser → [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

🎉 You’ll see Django’s “Congratulations” page — meaning your project works perfectly.

---

## 🧩 **7. Create a Django App**

Let’s create an app inside the project — e.g., “students”.

```bash
python manage.py startapp students
```

Your project structure now looks like this:

```
schoolportal/
│
├── manage.py
├── schoolportal/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── students/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations/
    ├── models.py
    ├── tests.py
    └── views.py
```

---

## 📂 **8. Understanding App Structure**

| File            | Purpose                                |
| --------------- | -------------------------------------- |
| **admin.py**    | Register models for Django admin panel |
| **apps.py**     | App configuration                      |
| **models.py**   | Define database models (tables)        |
| **views.py**    | Define how to handle web requests      |
| **migrations/** | Track database schema changes          |
| **tests.py**    | For writing unit tests                 |

---

## ⚙️ **9. Register the App in `settings.py`**

Every new app must be registered so Django can recognize it.

Open `schoolportal/settings.py`
Find the section named `INSTALLED_APPS` and add `'students'` to it:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Custom Apps
    'students',
]
```

---

## 🧠 **10. Create Your First View**

Open `students/views.py` and write:

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to the Student Portal</h1>")
```

---

## 🌐 **11. Create URL Routing for the App**

Inside your `students` folder, create a new file called `urls.py`.

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

---

## 🔗 **12. Link App URLs to the Project**

Open `schoolportal/urls.py` and include the `students` app:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('students.urls')),  # Root route
]
```

---

## ▶️ **13. Run the Server**

Now run:

```bash
python manage.py runserver
```

Open your browser → [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

✅ Output:

```
Welcome to the Student Portal
```

🎉 Congratulations! You’ve successfully:

* Created a Django project (`schoolportal`)
* Created an app (`students`)
* Linked routes
* Displayed your first webpage

---

## 🧩 **14. Practical Mini Exercise**

Try creating additional pages:

1. **About Page**

   * Add a new view `about(request)` in `views.py`
   * Create a route `/about` in `urls.py`
   * Display “This is the About Page”

2. **Contact Page**

   * Add a route `/contact`
   * Display contact details

✅ Test all pages in your browser.

---

## 💾 **15. Database Setup (Bonus)**

By default, Django uses **SQLite**.
Run migrations to set up the default database:

```bash
python manage.py migrate
```

✅ Output:

```
Applying auth.0001_initial... OK
...
```

---

## 🧍‍♂️ **16. Create a Superuser (Admin Account)**

```bash
python manage.py createsuperuser
```

Enter:

```
Username: admin
Email: admin@example.com
Password: ********
```

Then run the server and visit:
👉 [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

Login with your new credentials.
You now have access to Django’s built-in **Admin Dashboard**.

---

## ✅ **Summary**

| Command                                 | Description                |
| --------------------------------------- | -------------------------- |
| `django-admin startproject projectname` | Create a new project       |
| `python manage.py startapp appname`     | Create a new app           |
| `python manage.py runserver`            | Run the development server |
| `python manage.py migrate`              | Apply database migrations  |
| `python manage.py createsuperuser`      | Create admin user          |
| `python manage.py shell`                | Open Django’s Python shell |

---

## 🧠 **Next Lesson Suggestion**

Would you like to proceed next with:
**“Creating Models, Migrations, and Using Django ORM (Database)”**
→ where we define models (tables), migrate them, and interact with data in Python?

That’s the next logical step after creating your project and app.
