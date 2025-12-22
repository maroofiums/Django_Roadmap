# 🧠 Week 14: Scaling, Deployment & Production (7 Days)

> **Goal:** “Local project → Internet pe live, secure, scalable app”

---

## 🗓️ Day 1 — Switch Database to PostgreSQL (Industry MUST)

### 🔍 Concept

SQLite sirf learning ke liye hota hai.
**Production = PostgreSQL**

### 🔧 Steps

1. Install PostgreSQL
2. Install driver:

```bash
pip install psycopg2-binary
```

3. `settings.py`

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "mydb",
        "USER": "postgres",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```

4. Migrate:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 🧠 Advice

❌ SQLite in production
✅ PostgreSQL always (stable + scalable)

---

## 🗓️ Day 2 — Clean & Scalable CRUD (API + Views)

### 🔍 Focus

* Reusable CRUD
* Class Based Views / DRF ViewSets
* No duplicate logic

### Best Practice

* HTML → CBVs
* API → DRF ViewSets

```python
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

### 🧠 Advice

❌ Function views everywhere
✅ CBV + ViewSets = clean architecture

---

## 🗓️ Day 3 — Signals + Channels (Real Automation)

### 🔔 Signals

* Auto profile creation
* Notifications
* Cleanup logic

```python
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
```

### ⚡ Channels

* Live notifications
* Real-time updates
* Chat / activity feed

```python
async def connect(self):
    await self.accept()
```

### 🧠 Advice

Signals = backend automation
Channels = real-time power

---

## 🗓️ Day 4 — Redis Caching (Performance Boost 🚀)

### 🔍 Why Redis?

* Fast
* Used by Netflix, Twitter, Instagram

### Setup

```bash
pip install django-redis
```

```python
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
    }
}
```

### Use

```python
from django.views.decorators.cache import cache_page

@cache_page(60 * 5)
def home(request):
    ...
```

### 🧠 Advice

❌ DB hits on every request
✅ Cache frequently used pages

---

## 🗓️ Day 5 — Dockerize Django 🐳

### 🔍 Why Docker?

* Same app everywhere
* No “works on my machine” problem

### `Dockerfile`

```dockerfile
FROM python:3.13
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["gunicorn", "project.wsgi:application", "--bind", "0.0.0.0:8000"]
```

### Run

```bash
docker build -t django-app .
docker run -p 8000:8000 django-app
```

### 🧠 Advice

Docker = mandatory for backend jobs

---

## 🗓️ Day 6 — Security Best Practices 🔐

### MUST DO

* `DEBUG = False`
* Use `.env` file
* CSRF protection
* Password hashing (default Django)
* Allowed hosts

```python
ALLOWED_HOSTS = ["yourdomain.com"]
```

### 🧠 Advice

Security ignorance = app death 💀
Django gives tools — use them properly.

---

## 🗓️ Day 7 — Final Project (Pick ONE)

### 🥇 BEST PICK (Recommended for you)

### ✅ **Todo App with AI Integration**

#### Why?

* Simple UI
* Powerful backend
* AI = modern + impressive

#### Features

* CRUD Todos
* AI task summary (OpenAI)
* API + frontend
* PostgreSQL
* Redis cache
* Docker
* Deployed

---
