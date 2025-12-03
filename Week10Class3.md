
---

# ⭐ **DJANGO SIGNALS (Comprehensive Guide)**

Django **Signals** allow parts of an application to communicate with each other. They are used to perform an action **automatically** when a specific event happens in the system.

They help you write code that reacts to occurrences such as:

* A user is created
* A model is saved
* A model is deleted
* A request is started or finished
* A password is changed
* A session is created

Think of signals as **event listeners**.

---

# 🔵 1. **Why Signals?**

Use signals when you want to do something automatically without modifying existing logic.

### Examples:

✔ Automatically create a **UserProfile** when a new User is registered
✔ Send an email when a new order is placed
✔ Log activity when a user logs in
✔ Clear cache when a model is updated
✔ Generate notifications when a post is liked

---

# 🔵 2. **Types of Django Signals**

Django provides common built-in signals:

### ✔ Model Signals

* `pre_save`
* `post_save`
* `pre_delete`
* `post_delete`
* `m2m_changed`

### ✔ Request/Response Signals

* `request_started`
* `request_finished`

### ✔ User Authentication Signals

* `user_logged_in`
* `user_logged_out`
* `user_login_failed`

You can also create **custom signals**.

---

# 🔵 3. **Creating a Basic Signal (post_save)**

Let's say we want to automatically create a `Profile` whenever a new `User` is created.

---

## Step 1 — Create `signals.py` inside an app

```
myapp/
│── models.py
│── signals.py
│── apps.py
```

---

## Step 2 — Write the signal

### In `signals.py`

```python
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print("Profile created!")
```

Explanation:

* `sender=User` — we are listening for User model saves
* `created=True` — ensures it only runs for new users
* It creates a profile automatically

---

# 🔵 4. **Connecting Signals in apps.py**

### In `apps.py`

```python
from django.apps import AppConfig

class MyappConfig(AppConfig):
    name = 'myapp'

    def ready(self):
        import myapp.signals
```

### Don’t forget to register the app in `settings.py`:

```python
INSTALLED_APPS = [
    'myapp.apps.MyappConfig',
]
```

Without this step — signals **will not run**.

---

# 🔵 5. **post_delete Example**

Automatically delete a user’s profile when the user is deleted.

```python
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Profile

@receiver(post_delete, sender=Profile)
def delete_profile_picture(sender, instance, **kwargs):
    if instance.avatar:
        instance.avatar.delete()
```

---

# 🔵 6. **pre_save Example**

You can modify data **before saving**.

```python
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Post

@receiver(pre_save, sender=Post)
def capitalize_title(sender, instance, **kwargs):
    instance.title = instance.title.title()
```

If user saves `"my first post"` → Django automatically saves `"My First Post"`.

---

# 🔵 7. **m2m_changed Example**

Track many-to-many relationship updates.

```python
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Course

@receiver(m2m_changed, sender=Course.students.through)
def course_students_updated(sender, instance, action, **kwargs):
    print(f"Action: {action} on course {instance}")
```

Possible actions:

* `post_add`
* `pre_remove`
* `post_clear`, etc.

---

# 🔵 8. **User Authentication Signals**

### User logs in:

```python
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver

@receiver(user_logged_in)
def on_login(sender, request, user, **kwargs):
    print(f"{user} just logged in!")
```

---

### User logs out:

```python
from django.contrib.auth.signals import user_logged_out
@receiver(user_logged_out)
def on_logout(sender, request, user, **kwargs):
    print(f"{user} has logged out!")
```

---

# 🔵 9. **Request-Based Signals**

### Request started:

```python
from django.core.signals import request_started
from django.dispatch import receiver

@receiver(request_started)
def on_request_started(sender, **kwargs):
    print("A request has started!")
```

### Request finished:

```python
from django.core.signals import request_finished

@receiver(request_finished)
def on_request_finished(sender, **kwargs):
    print("A request just finished.")
```

---

# 🔵 10. **Creating Custom Signals**

### Step 1: Create the signal

```python
from django.dispatch import Signal

order_completed = Signal()
```

---

### Step 2: Send the signal

```python
order_completed.send(sender=None, order_id=12, user="Adewale")
```

---

### Step 3: Listen for the signal

```python
@receiver(order_completed)
def order_handler(sender, order_id, user, **kwargs):
    print(f"Order {order_id} completed by {user}")
```

---

# 🔵 11. **Best Practices for Django Signals**

✔ Use signals only for "side effects"
✔ Don’t put business logic in Signals
✔ Avoid making signals too heavy (emails, loops, big queries)
✔ Add error handling inside signal receivers
✔ Make sure your app's `apps.py` loads signals
✔ Use logging instead of print in production
✔ For large apps, group signals in modules

---

# 🟢 **Practical Exercises (10–12 Tasks)**

1. Create a signal that logs when a new user signs up.
2. Create a profile automatically for every user (post_save).
3. Send a welcome email after user creation using a signal.
4. Automatically delete uploaded images when a model is deleted.
5. Capitalize blog post titles using pre_save.
6. Track how many times a user logs in.
7. Track when a blog post is liked using a custom signal.
8. Create middleware + signal combo to log IP + request time.
9. Use a signal to clear cache when a model is updated.
10. Use m2m_changed to track when a user joins a group.
11. Create a custom signal for "payment completed".
12. Log every request start and end using signals.

---

