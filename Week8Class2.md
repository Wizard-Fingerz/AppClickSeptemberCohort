
---

# 🎨 **Django Static Files & Media Management**

---

## 🧠 **1. What are Static and Media Files?**

| Type             | Purpose                                          | Examples                                  |
| ---------------- | ------------------------------------------------ | ----------------------------------------- |
| **Static Files** | Files used for **front-end styling and scripts** | CSS, JavaScript, images used in templates |
| **Media Files**  | Files **uploaded by users**                      | Profile pictures, documents, PDFs         |

---

## ⚙️ **2. Setting Up Static Files**

### 2.1 Create a Static Folder

In your Django app (`myapp`):

```
myapp/
    static/
        myapp/
            css/
                style.css
            js/
                script.js
            images/
                logo.png
```

> Note: Static folder is **inside the app** and organized by app name to avoid conflicts.

---

### 2.2 Update Settings

In `settings.py`:

```python
STATIC_URL = '/static/'

# Optional — For production use
STATICFILES_DIRS = [
    BASE_DIR / "static",  # Global static folder
]

STATIC_ROOT = BASE_DIR / "staticfiles"  # Collected static files for deployment
```

---

### 2.3 Load Static Files in Templates

1. Load static tag at the top:

```html
{% load static %}
```

2. Use static files in template:

```html
<link rel="stylesheet" href="{% static 'myapp/css/style.css' %}">
<script src="{% static 'myapp/js/script.js' %}"></script>
<img src="{% static 'myapp/images/logo.png' %}" alt="Logo">
```

✅ This ensures Django knows where to look for files.

---

### 2.4 Collect Static Files (For Deployment)

```bash
python manage.py collectstatic
```

* Collects all static files from apps into `STATIC_ROOT`
* Essential for serving files in **production**.

---

## 🧩 **3. Media Files (User Uploads)**

### 3.1 Create a Media Folder

At the **project root**:

```
media/
```

### 3.2 Update Settings

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

* `MEDIA_URL` → URL path to access media
* `MEDIA_ROOT` → Physical directory where files are stored

---

### 3.3 Model for File Uploads

```python
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/')
```

* `upload_to` → subfolder inside `MEDIA_ROOT`

---

### 3.4 Handling Media in Views

No special changes needed — forms handle file uploads:

```python
from .forms import ProfileForm

def upload_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'accounts/upload.html', {'form': form})
```

> **Note:** `request.FILES` is required for file uploads.

---

### 3.5 Template for Media Files

```html
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Upload</button>
</form>

{% if user.profile.profile_picture %}
<img src="{{ user.profile.profile_picture.url }}" alt="Profile Picture">
{% endif %}
```

* `enctype="multipart/form-data"` is **mandatory** for file uploads
* Access the uploaded file with `.url` in templates

---

### 3.6 Serving Media During Development

In `urls.py` (project-level):

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... your urls
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

✅ Only for **development**. In production, serve media via **web server** (Nginx, Apache).

---

## 🧠 **4. Combining Static & Media in Templates**

Example:

```html
{% load static %}
<link rel="stylesheet" href="{% static 'myapp/css/style.css' %}">

<img src="{% if user.profile.profile_picture %}
{{ user.profile.profile_picture.url }}
 
 {% else %}
 
 {% static 'myapp/images/default.png' %}
 {% endif %}"
  alt="Profile">
```

* Shows user-uploaded image if exists
* Else shows a default static image

---

## 🧩 **5. Best Practices**

1. Keep **static files organized by app name**.
2. Keep **media files separate** from static files.
3. Use `{% load static %}` and `.url` for references.
4. Never store user-uploaded files inside static directories.
5. For production:

   * Use `collectstatic` for static files
   * Serve media files via a **web server**
6. Always validate uploaded files for security (file type, size).

---

## 🧰 **6. Exercises**

1. Add a CSS file to your app and link it to a template.
2. Add a JS file and trigger an alert when the page loads.
3. Add a logo image as a static file and display it on the navbar.
4. Create a **profile model** with an image upload field.
5. Create a form for users to upload profile pictures.
6. Display the uploaded image in the user profile template.
7. Provide a **default image** if the user hasn’t uploaded one.
8. Add multiple media files for a model (e.g., documents, images).
9. Ensure media files are only accessible to logged-in users.
10. Test `collectstatic` and verify all static files are correctly collected.

---

## ✅ **Summary**

| Concept            | Key Points                                                     |
| ------------------ | -------------------------------------------------------------- |
| **Static Files**   | CSS, JS, images for site design, stored in `static/`           |
| **Media Files**    | User uploads, stored in `MEDIA_ROOT`, accessed via `MEDIA_URL` |
| **Template Usage** | `{% static %}` for static, `{{ file.url }}` for media          |
| **Forms**          | `enctype="multipart/form-data"` for uploads                    |
| **Development**    | Use `static()` for media serving during DEBUG                  |
| **Production**     | Use `collectstatic` and serve media with web server            |

---

After mastering **static & media files**, your Django apps can now:

* Include **styling** (CSS), **interactivity** (JS), and **images**
* Accept **user uploads** like profile pictures, documents, and media
* Serve files correctly in **development and production**

---

