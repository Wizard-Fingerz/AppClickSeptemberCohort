
---

# 🧱 **Setting Up a Virtual Environment and Installing Django**

---

## 🧠 **1. What is a Virtual Environment?**

A **virtual environment** is an **isolated workspace** that allows you to install Python packages for a specific project — without affecting other projects or your system Python.

Think of it like a *sandbox* where:

* Each project can have its own dependencies (e.g., Django 5.1 vs Django 4.2)
* You avoid “dependency conflicts”
* You keep your system clean and organized

---

## ⚙️ **2. Check Your Python Installation**

Open your terminal or command prompt and type:

```bash
python --version
```

✅ **Expected Output (example):**

```
Python 3.12.2
```

If it shows an error, install Python first from [https://python.org/downloads](https://python.org/downloads) and ensure the “Add to PATH” option is checked during installation.

---

## 📦 **3. Install `virtualenv` (If Needed)**

While Python 3.3+ includes `venv` built-in, you can also install the more flexible `virtualenv` package.

### Option 1: Use built-in venv

No installation needed.

### Option 2: Install virtualenv manually

```bash
pip install virtualenv
```

---

## 🧩 **4. Create a Virtual Environment**

Navigate to your project folder in the terminal:

```bash
cd path/to/your/project
```

Then run:

```bash
python -m venv venv
```

✅ This creates a folder named **`venv/`** which contains a standalone Python environment.

---

## ▶️ **5. Activate the Virtual Environment**

### On **Windows**:

```bash
venv\Scripts\activate
```

### On **Mac/Linux**:

```bash
source venv/bin/activate
```

✅ **You’ll know it’s activated** when you see `(venv)` appear before your terminal prompt:

```
(venv) C:\Users\Adewale\myproject>
```

---

## 🧹 **6. Confirm the Environment**

Run:

```bash
where python        # On Windows
# or
which python        # On Mac/Linux
```

✅ It should point to your project’s `venv` directory — not the global Python installation.

---

## 📥 **7. Install Django**

Once the environment is active, install Django with pip:

```bash
pip install django
```

✅ **Output Example:**

```
Successfully installed Django-5.1
```

---

## 🧾 **8. Verify the Django Installation**

Check the installed Django version:

```bash
django-admin --version
```

✅ **Output Example:**

```
5.1
```

---

## 🏗️ **9. Create a New Django Project**

Now that Django is installed, create your first project:

```bash
django-admin startproject myproject
```

This will create a folder named `myproject` containing:

```
myproject/
    manage.py
    myproject/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

---

## ▶️ **10. Run the Development Server**

Navigate into your project directory:

```bash
cd myproject
python manage.py runserver
```

✅ **Output Example:**

```
Watching for file changes with StatReloader
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

Open your browser and visit:
👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

🎉 You’ll see the **“Congratulations! Django is installed successfully”** page.

---

## 🧰 **11. Deactivating the Virtual Environment**

When you’re done working:

```bash
deactivate
```

This returns you to your system Python environment.

---

## 📚 **12. Optional but Recommended Setup**

### Save installed dependencies:

```bash
pip freeze > requirements.txt
```

✅ This creates a file listing all installed packages (useful when deploying or sharing your project).

To reinstall them later:

```bash
pip install -r requirements.txt
```

---

## 🧠 **Summary**

| Step | Command                               | Purpose                        |
| ---- | ------------------------------------- | ------------------------------ |
| 1    | `python --version`                    | Check Python installation      |
| 2    | `python -m venv venv`                 | Create virtual environment     |
| 3    | `venv\Scripts\activate`               | Activate environment (Windows) |
| 4    | `pip install django`                  | Install Django                 |
| 5    | `django-admin startproject myproject` | Create new Django project      |
| 6    | `python manage.py runserver`          | Run development server         |
| 7    | `deactivate`                          | Exit environment               |

---

## 💡 **Practical Exercise**

1. Create a new virtual environment.
2. Install Django.
3. Create a project named `schoolportal`.
4. Run the server and visit it in your browser.
5. Deactivate your environment.

---

