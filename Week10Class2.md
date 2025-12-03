
# ⭐ **DJANGO MIDDLEWARE (Comprehensive Guide)**

We will cover:

1. What middleware is
2. Built-in Django middleware
3. How the middleware request/response cycle works
4. Creating custom middleware
5. Middleware ordering
6. Enabling/disabling middleware
7. Use cases & best practices
8. Practical exercises

Let's begin.

---

# 🔵 1. **What is Middleware in Django?**

Middleware is a **layer of processing** that sits between:

✔ The user's request → coming into Django
✔ Django’s response → going back to the user

In simple terms:

👉 Middleware = “Code that runs before and after every request.”

It can be used for:

* Authentication checks
* Logging
* Performance tracking
* Security features
* Request/response modification
* Blocking IP addresses
* Adding custom headers

---

# 🔵 2. **The Middleware Flow in Django**

Middleware runs in a specific order.

### **Request Phase:**

1. Request received
2. Middleware A → `process_request()`
3. Middleware B → `process_request()`
4. Middleware C → `process_request()`
5. View is called

---

### **Response Phase:**

1. View returns response
2. Middleware C → `process_response()`
3. Middleware B → `process_response()`
4. Middleware A → `process_response()`
5. Response sent to user

📌 This is called a **middleware stack**.

---

# 🔵 3. **Built-in Django Middleware (Important Ones)**

Located in `settings.py → MIDDLEWARE`

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]
```

### What they do:

### ✔ `SecurityMiddleware`

Enforces security headers (HTTPS, HSTS, clickjacking protection).

### ✔ `SessionMiddleware`

Enables session support.

### ✔ `CommonMiddleware`

Handles:

* URL rewriting
* ETags
* Trailing slashes

### ✔ `CsrfViewMiddleware`

Protects against Cross-Site Request Forgery.

### ✔ `AuthenticationMiddleware`

Attaches the authenticated user to the request (`request.user`)

### ✔ `MessageMiddleware`

Enables messaging framework:
`messages.success(request, "Saved!")`

---

# 🔵 4. **Creating Custom Middleware**

You can create middleware for:

* Logging
* Blocking users
* Modifying responses
* Tracking performance

### Step 1 — Create middleware file

`project/middleware.py`

```python
from django.http import HttpResponse

class BlockIPMiddleware:
    blocked_ips = ['127.0.0.2']

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')

        if ip in self.blocked_ips:
            return HttpResponse("Access Denied")

        response = self.get_response(request)
        return response
```

---

### Step 2 — Add to settings.py

```python
MIDDLEWARE.append('project.middleware.BlockIPMiddleware')
```

Now, the listed IPs will be blocked from accessing the website.

---

# 🔵 5. **Custom Middleware With Before/After Logic**

```python
class LogMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Before request:", request.path)

        response = self.get_response(request)

        print("After response:", response.status_code)

        return response
```

This logs all requests and responses.

---

# 🔵 6. **Middleware Order**

Middleware runs **top → bottom** on requests
and **bottom → top** on responses.

Thus:

* AuthenticationMiddleware must come AFTER SessionMiddleware
* CSRFMiddleware must come AFTER SessionMiddleware
* MessageMiddleware must come AFTER AuthenticationMiddleware

Wrong ordering can break your project!

---

# 🔵 7. **Disabling Middleware**

You can comment out unused middleware:

```python
# 'django.middleware.csrf.CsrfViewMiddleware',
```

But disabling CSRF is **never recommended** unless you are building an API.

---

# 🔵 8. **Example Use Cases of Middleware**

### ✔ 1. Block users by IP

### ✔ 2. Add custom headers

### ✔ 3. Measure site performance

### ✔ 4. Redirect certain users

### ✔ 5. Detect bots

### ✔ 6. Add additional security checks

### ✔ 7. Modify request/response data

---

# 🔵 9. **Practical Exercises (10 Tasks)**

1. Create middleware that logs every request path.
2. Create middleware that prints time taken to process a request.
3. Block specific IP addresses.
4. Create middleware that redirects all users to a “Maintenance Page”.
5. Add a custom HTTP header (`X-App-Version`) to every response.
6. Create middleware that blocks users who are not authenticated.
7. Limit access to your app between 9AM and 6PM (closing hours middleware).
8. Create middleware that logs errors into a file.
9. Strip any whitespace from all POST data using middleware.
10. Add geolocation-based blocking (block countries by IP prefix).

---

