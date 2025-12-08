from django.test import TestCase
from django.urls import reverse, path
from chatapp.models import ChatMessage
from chatapp.views import messages_list

urlpatterns = [
    path("messages/", messages_list, name="messages"),
]

class MessagesViewTest(TestCase):

    def test_messages_empty_list(self):
        response = self.client.get("/messages/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"messages": []})

    def test_messages_with_data(self):
        ChatMessage.objects.create(username="ali", message="Hello!")
        res = self.client.get("/messages/")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.json()["messages"]), 1)
