
---

# ⭐ **Django Admin Customization**

The Django admin is a powerful built-in interface for managing models. By default, it provides basic CRUD functionality. **Customizing the admin** makes it more user-friendly, efficient, and tailored to your project.

---

# 🔵 **1. Registering Models in Admin**

### Basic registration:

```python
# admin.py
from django.contrib import admin
from .models import Student

admin.site.register(Student)
```

Now, `Student` appears in the Django admin.

---

### Using `@admin.register` decorator:

```python
from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass
```

This allows **more customization** later.

---

# 🔵 **2. Customizing the Admin List View**

Admin list view shows all objects of a model.

### Common options:

```python
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'grade')  # columns shown
    list_display_links = ('name',)                 # clickable columns
    list_editable = ('grade',)                     # editable in list view
    list_filter = ('grade',)                       # filter sidebar
    search_fields = ('name', 'grade')             # search bar
    ordering = ('-id',)                            # default ordering
```

✅ **Explanation:**

* `list_display`: columns to show
* `list_display_links`: which column links to detail view
* `list_editable`: columns editable directly
* `list_filter`: adds sidebar filters
* `search_fields`: adds search box
* `ordering`: sort objects by field

---

# 🔵 **3. Customizing the Admin Form**

You can control **how the form looks** when adding or editing an object.

```python
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = ('name', 'age', 'grade')  # fields order in form
```

---

### Group fields with `fieldsets`:

```python
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'age')
        }),
        ('Academic Info', {
            'fields': ('grade',),
            'classes': ('collapse',)  # collapsible section
        }),
    )
```

---

# 🔵 **4. Inline Models**

For models with **ForeignKey relationships**, you can display related objects inline.

### Example:

```python
# models.py
class Course(models.Model):
    name = models.CharField(max_length=100)

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField()

# admin.py
from django.contrib import admin
from .models import Student, Enrollment

class EnrollmentInline(admin.TabularInline):
    model = Enrollment
    extra = 1  # number of extra empty forms

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [EnrollmentInline]
```

✅ TabularInline → horizontal layout
✅ StackedInline → vertical layout

---

# 🔵 **5. Custom Actions**

You can add **actions to admin list view**.

```python
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'grade')

    actions = ['make_senior']

    def make_senior(self, request, queryset):
        queryset.update(grade='Senior')
        self.message_user(request, "Selected students updated to Senior")
    make_senior.short_description = "Promote selected students to Senior"
```

Now you can select multiple students and run the action from the dropdown.

---

# 🔵 **6. Read-Only Fields**

Make certain fields **read-only** in admin:

```python
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
```

Useful for automatically generated fields.

---

# 🔵 **7. Customizing the Admin Site Appearance**

### Change site header and title:

```python
admin.site.site_header = "School Management Admin"
admin.site.site_title = "School Portal"
admin.site.index_title = "Dashboard"
```

This is visible in the top bar of admin pages.

---

# 🔵 **8. Using `prepopulated_fields`**

Automatically fill a field based on another field:

```python
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
```

Creates slug automatically from course name.

---

# 🔵 **9. List Display with Methods**

You can display **custom columns** in admin:

```python
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'grade', 'is_adult')

    def is_adult(self, obj):
        return obj.age >= 18
    is_adult.boolean = True  # show as icon
    is_adult.short_description = "Adult?"
```

---

# 🔵 **10. Advanced Filtering with `list_filter`**

Supports:

* Field filters (`grade`)
* Date filters (`date_joined`)
* Custom filters using classes

```python
from django.contrib.admin import SimpleListFilter

class AgeFilter(SimpleListFilter):
    title = 'age'
    parameter_name = 'age'

    def lookups(self, request, model_admin):
        return (
            ('teen', '13-19'),
            ('adult', '20+'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'teen':
            return queryset.filter(age__gte=13, age__lte=19)
        if self.value() == 'adult':
            return queryset.filter(age__gte=20)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_filter = (AgeFilter, 'grade')
```

---

# 🔵 **11. Admin Permissions**

* `add_modelname` → permission to add objects
* `change_modelname` → permission to edit objects
* `delete_modelname` → permission to delete objects

You can restrict **actions and visibility** based on user roles.

---

# 🔵 **12. Best Practices**

✔ Use inlines for related objects
✔ Use `list_display` and `search_fields` for usability
✔ Use `readonly_fields` for automatically generated data
✔ Add custom actions for repetitive tasks
✔ Use `prepopulated_fields` to reduce manual entry
✔ Organize forms with `fieldsets`
✔ Customize the admin header and index title for branding

---

# 🟢 **Practical Exercises (10–12 Tasks)**

1. Register a `Student` model and customize list_display.
2. Add search functionality for `Student` name.
3. Add filter by `grade` in list view.
4. Add `readonly_fields` for `id` and `created_at`.
5. Prepopulate slug field for `Course` from name.
6. Create inline for `Enrollment` under `Student`.
7. Add custom action to promote selected students to “Senior”.
8. Display a boolean column `is_adult` in the list view.
9. Group form fields with `fieldsets`.
10. Customize admin site header, title, and index title.
11. Implement a custom list filter for age ranges.
12. Restrict certain admin actions for non-staff users.

---
