
---

# ✅ **Django Caching — Comprehensive Notes**

Caching is a technique used to **store frequently accessed data temporarily** so that future requests for that data are served faster.
Django provides a powerful, flexible caching framework that helps you improve **performance, reduce database hits, and speed up page load time**.

---

# 🔶 **1. Why Use Caching?**

Caching helps to:

✔ Reduce server load
✔ Improve webpage response time
✔ Reduce repeated database queries
✔ Improve user experience
✔ Handle high traffic efficiently

Think of caching as saving a *shortcut* of expensive computations so you don’t redo them every time.

---

# 🔶 **2. Types of Caching in Django**

Django supports multiple caching backends:

| Cache Backend          | Description                                                 |
| ---------------------- | ----------------------------------------------------------- |
| **Memcached**          | Very fast, distributed caching system. Best for production. |
| **Redis Cache**        | Fast in-memory database; popular for large applications.    |
| **Database Cache**     | Stores cache data in a database table.                      |
| **File-Based Cache**   | Stores cached data in the file system.                      |
| **Local Memory Cache** | Default; stores cache in RAM per process.                   |

---

# 🔶 **3. Setting Up Caching**

You define caching settings in **settings.py**.

---

## ✅ **A. Local Memory Caching (Default)**

```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-cache'
    }
}
```

Good for development and small projects.

---

## ✅ **B. File-Based Caching**

```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
    }
}
```

Suitable when you don't want external services.

---

## ✅ **C. Database Caching**

1. Create a table for caching:

```bash
python manage.py createcachetable
```

2. Configure:

```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
    }
}
```

---

## ✅ **D. Memcached (Recommended for production)**

Install memcached library:

```bash
pip install python-memcached
```

Add config:

```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
```

---

# 🔶 **4. Levels of Caching in Django**

Django provides THREE LEVELS of caching:

---

## **1️⃣ Page Level Caching (Full Page Cache)**

Caches the **entire HTML page**.

### Setup:

Add to **urls.py**:

```python
from django.views.decorators.cache import cache_page
from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', cache_page(60)(views.homepage), name='home'),
]
```

This caches the *homepage* for **60 seconds**.

---

## **2️⃣ View Level Caching (Per-View Cache)**

Caches the output of *individual views*.

Example:

```python
from django.views.decorators.cache import cache_page

@cache_page(120)
def product_list(request):
    ...
```

This caches the view for **2 minutes**.

---

## **3️⃣ Template Fragment Caching**

Used when only a *portion of a template* is expensive to generate.

### Example:

```html
{% load cache %}

{% cache 300 product_section %}
    <div>
        {% for product in products %}
            <p>{{ product.name }}</p>
        {% endfor %}
    </div>
{% endcache %}
```

This caches only the **product section** for 5 minutes.

---

# 🔶 **5. Low-Level Cache API**

Django allows you to manually interact with the cache using the **cache object**.

Import cache:

```python
from django.core.cache import cache
```

---

## ✅ **A. Setting a value in cache**

```python
cache.set('username', 'Adewale', 60)  # store for 60 seconds
```

---

## ✅ **B. Getting a value**

```python
user = cache.get('username')
```

---

## ✅ **C. Setting a default value if not exists**

```python
user = cache.get_or_set('username', 'Guest', 60)
```

---

## ✅ **D. Deleting a value**

```python
cache.delete('username')
```

---

## ✅ **E. Checking if a cache key exists**

```python
cache.has_key('username')
```

---

# 🔶 **6. Caching with Database Querysets**

Django does NOT automatically cache querysets.

But you can cache them manually:

```python
products = cache.get('products')

if not products:
    products = Product.objects.all()
    cache.set('products', products, 120)
```

This avoids repeated database hits.

---

# 🔶 **7. Cache Versioning**

Useful when replacing old cached data.

```python
cache.set('my_key', 'value1', version=1)
cache.set('my_key', 'value2', version=2)
```

---

# 🔶 **8. Clearing Cache**

Clear all cache data:

```python
cache.clear()
```

---

# 🔶 **9. Pros & Cons of Caching**

## 👍 **Advantages**

* Super-fast response times
* Less load on database
* Handles more users
* Reduces server cost

## 👎 **Disadvantages**

* Requires memory
* Data may get outdated
* Needs careful invalidation strategies

---

# 🔶 **10. Best Practices for Django Caching**

✔ Cache expensive operations (DB queries, heavy templates)
✔ Don’t overcache everything
✔ Use fragment caching for dynamic pages
✔ Use Redis or Memcached for large projects
✔ Set appropriate cache timeout
✔ Always test cache invalidation logic

---
