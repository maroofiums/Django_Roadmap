## **Week 13: Submodules Deep Dive – 7-Day Plan**

### **Day 1 — File Uploads (FileField & ImageField)**

**Goal:** Learn how to handle file uploads (images, docs) in Django.

**Steps:**

1. Create a model with `FileField` or `ImageField`.

   ```python
   class Document(models.Model):
       title = models.CharField(max_length=100)
       file = models.FileField(upload_to='uploads/')
       uploaded_at = models.DateTimeField(auto_now_add=True)
   ```
2. Make a form for uploads:

   ```python
   from django import forms
   from .models import Document

   class DocumentForm(forms.ModelForm):
       class Meta:
           model = Document
           fields = ['title', 'file']
   ```
3. Create a view to handle uploads (GET → show form, POST → save file).
4. Update `urls.py`.
5. Make template with `<input type="file">` and `enctype="multipart/form-data"`.
6. Test file upload in the browser.

**Pro Tip:** Always clean old uploaded files when deleting objects — avoids unused files piling up.

---

### **Day 2 — Messages Framework**

**Goal:** Add flash messages like success/error alerts.

**Steps:**

1. Import Django messages in views:

   ```python
   from django.contrib import messages
   ```
2. Use messages in views:

   ```python
   messages.success(request, "Your post was saved!")
   messages.error(request, "Something went wrong.")
   ```
3. In your template, display messages:

   ```html
   {% if messages %}
       {% for message in messages %}
           <div class="alert alert-{{ message.tags }}">{{ message }}</div>
       {% endfor %}
   {% endif %}
   ```

**Tip:** Combine with Bootstrap alerts for nice styling.

---

### **Day 3 — Custom Template Tags & Filters**

**Goal:** Learn how to create reusable logic inside templates.

**Steps:**

1. Create a `templatetags` folder in your app.
2. Example: create `my_filters.py`:

   ```python
   from django import template

   register = template.Library()

   @register.filter
   def truncate_chars(value, max_length):
       return value[:max_length] + "..." if len(value) > max_length else value
   ```
3. Load in template:

   ```html
   {% load my_filters %}
   {{ post.content|truncate_chars:50 }}
   ```

**Tip:** Filters are perfect for formatting data without bloating views.

---

### **Day 4 — Email Sending**

**Goal:** Send email via Django.

**Steps:**

1. Configure email in `settings.py`:

   ```python
   EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"  # for dev
   EMAIL_HOST = "smtp.gmail.com"
   EMAIL_PORT = 587
   EMAIL_USE_TLS = True
   EMAIL_HOST_USER = "<your_email>"
   EMAIL_HOST_PASSWORD = "<your_password>"
   ```
2. Send email in views:

   ```python
   from django.core.mail import send_mail

   send_mail(
       "Subject here",
       "Here is the message.",
       "from@example.com",
       ["to@example.com"],
       fail_silently=False,
   )
   ```

**Tip:** Use console backend during development to avoid spamming real emails.

---

### **Day 5 — Management Commands**

**Goal:** Automate tasks with custom commands.

**Steps:**

1. Create folder `management/commands` inside your app.
2. Example command: `myapp/management/commands/hello.py`

   ```python
   from django.core.management.base import BaseCommand

   class Command(BaseCommand):
       help = "Prints Hello World"

       def handle(self, *args, **kwargs):
           self.stdout.write("Hello World!")
   ```
3. Run in terminal:

   ```bash
   python manage.py hello
   ```

**Tip:** Useful for cron jobs, data imports, or seeding fake data.

---

### **Day 6 — Internationalization (i18n)**

**Goal:** Make your app multi-language ready.

**Steps:**

1. Mark strings in code:

   ```python
   from django.utils.translation import gettext_lazy as _
   title = models.CharField(max_length=100, verbose_name=_("Title"))
   ```
2. Mark strings in templates:

   ```html
   {% load i18n %}
   <h1>{% trans "Welcome" %}</h1>
   ```
3. Run commands to generate `.po` files, translate, and compile:

   ```bash
   django-admin makemessages -l es
   django-admin compilemessages
   ```
4. Switch languages via `LANGUAGE_CODE` or `LocaleMiddleware`.

**Tip:** Start with one secondary language (like Urdu) and expand later.

---

### **Day 7 — Revision + Mini Project**

**Mini Project Idea:**
Build a **File Upload + Email Notification App**:

* Upload a document.
* Auto-send an email notification.
* Show success/failure messages.
* Use a custom template filter to truncate file names.

---