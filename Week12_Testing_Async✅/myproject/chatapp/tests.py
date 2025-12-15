from django.test import TestCase
from django.contrib.auth.models import User
from .models import Room, Message

class ChatModelsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="12345"
        )
        self.room = Room.objects.create(name="general")

    def test_room_created(self):
        self.assertEqual(self.room.name, "general")

    def test_message_created(self):
        msg = Message.objects.create(
            room=self.room,
            user=self.user,
            content="Hello World"
        )
        self.assertEqual(msg.content, "Hello World")
        self.assertEqual(msg.user.username, "testuser")
from django.urls import reverse

class ChatViewsTest(TestCase):

    def test_home_page_status(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
