from django.test import TestCase
from chatapp.models import ChatMessage

class ChatMessageModelTest(TestCase):

    def test_create_message(self):
        msg = ChatMessage.objects.create(
            username="maroof",
            message="Hello testing world!"
        )

        self.assertEqual(msg.username, "maroof")
        self.assertEqual(ChatMessage.objects.count(), 1)
        self.assertTrue(msg.timestamp)
