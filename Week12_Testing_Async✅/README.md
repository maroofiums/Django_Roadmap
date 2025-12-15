# ⭐ **Week 12 — Testing & Async (Day-by-Day Full Plan)**

Goal: Tum Django ko **serious backend developer level** pe use karna start karo → bugs kam, code reliable, aur real-time features add karne wale.

---

# 🟩 **Day 1 — Django TestCase (Unit Tests Basics)**

*Aim: Test samajhna — kya hota hai, kyun likhte hain, aur kaise likhte hain.*

### 🔥 Concepts

* TestCase vs SimpleTestCase
* Setup data
* Testing models
* Testing views (status codes, content)

### 🧠 Step-by-step:

1. **Test create karo**

   ```
   myapp/tests/test_models.py
   myapp/tests/test_views.py
   ```

2. **Model test example:**

```python
from django.test import TestCase
from django.contrib.auth.models import User
from myapp.models import Post

class PostModelTest(TestCase):
    def test_post_creation(self):
        user = User.objects.create_user("maroof")
        post = Post.objects.create(user=user, title="Test", content="Hello")
        self.assertEqual(post.title, "Test")
```

3. **View test example:**

```python
class HomeViewTest(TestCase):
    def test_home_status(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
```

### ✔ Advice:

* Tests ko “useless chore” mat samajhna, yeh production me **life-saver** hotay hain.
* Har new feature ke sath **ek chota test** likho.

---

# 🟦 **Day 2 — Pytest + pytest-django**

*Aim: Modern developer ki testing style — fast, clean, readable.*

### 🔥 Concepts

* Pytest fixtures
* pytest-django setup
* In-built pytest features (asserts, factories etc.)

### 📦 Install:

```
pip install pytest pytest-django
```

### 🔧 pytest.ini

```
[pytest]
DJANGO_SETTINGS_MODULE = myproject.settings
```

### 🧪 Simple pytest example:

```python
import pytest
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_user_creation():
    user = User.objects.create(username="mrf")
    assert user.username == "mrf"
```

### ✔ Advice:

* Pytest >> Django TestCase (speed + readability)
* Aage chal ke tum factory_boy bhi use kar sakte ho for realistic test data.

---

# 🟨 **Day 3 — Django Channels (Async WebSockets Intro)**

*Aim: Real-time communication ka basic architecture samajhna.*

### 🔥 Concepts

* ASGI vs WSGI
* WebSockets kya hotay hain
* channels layers (in-memory or Redis)

### ⚙ Install:

```
pip install channels
```

### ASGI config:

`project/asgi.py` me:

```python
import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from myapp.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(websocket_urlpatterns),
})
```

### routing.py

```python
from django.urls import path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    path("ws/chat/", ChatConsumer.as_asgi()),
]
```

### Consumer (basic echo test)

```python
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(json.dumps({"message": "Connected!"}))
```

### ✔ Advice:

* Pehle simple “echo” consumer banao → phir group chat.
* Local testing → browser ya Postman WebSockets se.

---

# 🟩 **Day 4 — Real-time Chat (Rooms + Broadcasting)**

*Aim: Functional chat app build karna.*

### 🔥 Concepts

* Group Add / Group Send
* Room-based communication
* Users join/leave messages
* Frontend JS WebSocket client

### ChatConsumer (full working)

```python
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = "global_chat"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )

        await self.accept()

    async def receive(self, text_data):
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "text": text_data,
            }
        )

    async def chat_message(self, event):
        await self.send(event["text"])
```

### JS Client Example:

```javascript
let socket = new WebSocket("ws://127.0.0.1:8000/ws/chat/");

socket.onmessage = function(e){
    console.log("Message:", e.data);
}

socket.onopen = function(){
    socket.send("Hello!");
}
```

### ✔ Advice:

* Group chat implement ho jaye → tum 70% realtime skills cover kar chuke.
* Next level: Redis channel layer (scalable).

---

# 🟥 **Day 5 — Notifications + Redis Setup + Deployment Strategy**

*Aim: Professional-level real-time features.*

### 🔥 Concepts

* Redis as Channel Layer
* Real-time notifications
* Chat + Notification mix
* Testing async consumers

### Install:

```
pip install channels-redis
```

### settings.py

```python
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}
```

### Notification consumer example:

```python
class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user_group = f"user_{self.scope['user'].id}"
        await self.channel_layer.group_add(self.user_group, self.channel_name)
        await self.accept()
```

### ✔ Advice:

* Real-time notifications = real-world, high-impact feature
* Channels + Redis = **Google-level scalable architecture**

---

# 🟦 **Mini Project — Real-Time Chat App**

Features:

* Login + chat room
* Real-time message broadcasting
* Notifications when user joins
* Redis event layer
* Pytest async tests
