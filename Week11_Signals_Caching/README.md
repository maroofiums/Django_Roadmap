# Week11_Signals_Caching

# ⭐ **DAY 1 — Signals: Auto Create Profile**

### 📌 Folder structure:

```
myapp/
    models.py
    signals.py
    apps.py
    __init__.py
```

---

## 1️⃣ **models.py**

```python
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} Profile"
```

---

## 2️⃣ **signals.py**

```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
```

---

## 3️⃣ **apps.py**

```python
from django.apps import AppConfig

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self):
        import myapp.signals
```

---

## 4️⃣ ****init**.py**

```python
default_app_config = "myapp.apps.MyappConfig"
```

---

# ⭐ **DAY 2 — Signals: Email Notification (Example)**

### 👉 Jab koi new Post create ho, admin ko email chalay

## signals.py (same file me add)

```python
from django.core.mail import send_mail
from .models import Post

@receiver(post_save, sender=Post)
def notify_admin(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject="New post created",
            message=f"Title: {instance.title}",
            from_email="noreply@blog.com",
            recipient_list=["admin@example.com"],
        )
```

👉 Tip: Development me real email ke liye
`python -m smtpd -n -c DebuggingServer localhost:1025`

---

# ⭐ **DAY 3 — Basic Caching (Per-View Cache)**

## settings.py

```python
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "local-cache"
    }
}
```

## views.py

```python
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from .models import Post

@method_decorator(cache_page(60 * 2), name='dispatch')  # 2 minutes cache
class CachedPostListView(ListView):
    model = Post
    template_name = "posts/post_list.html"
```

✔ Ab list view **2 minutes ke liye cache** ho jayega = faster page loads.

---

# ⭐ **DAY 4 — Template Fragment Caching**

Example: sirf post list ka ek part cache karo.

### Template:

```html
{% load cache %}

{% cache 120 post_list_fragment %}
    {% for post in posts %}
        <p>{{ post.title }}</p>
    {% endfor %}
{% endcache %}
```

✔ Ye page ka sirf yeh block **120 seconds** cache karega.

---

# ⭐ **DAY 5 — Redis Caching (Fastest & Scalable)**

Install:

```
pip install django-redis
```

settings.py:

```python
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
```

View example:

```python
from django.core.cache import cache

def get_expensive_data():
    data = cache.get("stats")
    if not data:
        print("Querying DB...")
        data = {"users": 500, "posts": 120}
        cache.set("stats", data, timeout=60)
    return data
```

---

# ⭐ **DAY 6 — Mini Project: Blog + Signals + Cache**

Tumhari blog app ke andar:

✔ Profile auto create
✔ Post create par email notification
✔ List view caching
✔ Fragment caching
✔ Redis caching enabled

---

# ⭐ **DAY 7 — Revision + Cleanup**

• Signals ka flow samajho
• Cache kis jagah use karna chahiye
• Redis vs Local cache difference
• Performance improvements measure karo

---

