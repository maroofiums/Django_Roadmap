# ✅ **Week 10 — Django REST Framework (DRF)**

**Goal:** Apna Blog App ka complete REST API banana (List, Detail, Create, Update, Delete).

---

# **📌 Day 1 — DRF Install + Basic Serializer + APIView Intro**

**Concepts:**

* Install DRF
* Settings update
* Serializer kya hota hai?
* APIView basics (get/post)

**Code:**

### **1. Install DRF**

```bash
pip install djangorestframework
```

### **2. settings.py add**

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

### **3. Create serializer**

`blog/api/serializers.py`

```python
from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at']
```

### **4. Simple APIView**

`blog/api/views.py`

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from blog.models import Post
from .serializers import PostSerializer

class PostListAPI(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
```

### **5. URL**

```python
path("api/posts/", PostListAPI.as_view())
```

---

# **📌 Day 2 — ModelSerializer + Detail API**

**Concepts:**

* ModelSerializer deep explanation
* Retrieving single item
* Error handling (404)

**Code:**

### Detail API

```python
class PostDetailAPI(APIView):
    def get(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=404)

        serializer = PostSerializer(post)
        return Response(serializer.data)
```

---

# **📌 Day 3 — API Create + Update + Delete**

**Concepts:**

* POST (Create)
* PUT/PATCH (Update)
* DELETE
* Validation handling

**Code:**

### Create API

```python
class PostCreateAPI(APIView):
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
```

### Update API

```python
class PostUpdateAPI(APIView):
    def put(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
```

### Delete API

```python
class PostDeleteAPI(APIView):
    def delete(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response({"message": "deleted"})
```

---

# **📌 Day 4 — ViewSets + Routers (Modern, Clean, Best Practice)**

**Concepts:**

* DRF ViewSets
* Routers
* Automatic URL generation

**Code:**

### ViewSet

```python
from rest_framework import viewsets

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

### Router

```python
from rest_framework.routers import DefaultRouter
from blog.api.views import PostViewSet

router = DefaultRouter()
router.register("posts", PostViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
```

**Boom!** All CRUD in 5 lines.
Best practice for production systems.

---

# **📌 Day 5 — Permissions + Authentication**

**Concepts:**

* AllowAny
* IsAuthenticated
* Custom Permissions
* Only owner can update/delete

**Code:**

### Settings:

```python
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ]
}
```

You can also add simple Auth login:

```
/api-auth/login/
```

---

# **📌 Day 6 — Mini Project: Complete Blog REST API**

Iss din tum:

✅ Blog Post List API
✅ Blog Post Detail API
✅ Create — Update — Delete
✅ Router + ViewSet
✅ Permissions
✅ Testing via Postman / Thunder Client

Sab ek jagah clean and real-world style.

---

# **📌 Day 7 — Revision + API Documentation (Schema)**

**Concepts:**

* DRF built-in API docs
* Schema generation
* Recheck all endpoints
* Bug fixing

**Add drf-spectacular (optional pro-level):**

```bash
pip install drf-spectacular
```

---
