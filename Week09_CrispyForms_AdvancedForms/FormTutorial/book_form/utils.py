from faker import Faker
from .models import Book
from django.contrib.auth.models import User
from django.utils import timezone
import random

fake = Faker()

def create_fake_user(count=1):
    users = []
    for _ in range(count):
        username = fake.user_name()
        email = fake.email()
        password = "password123"  
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        users.append(user)
    return users


def create_fake_books(count=1, owners=None):
    books = []
    if owners is None:
        owners = list(User.objects.all())
        if not owners:
            owners = create_fake_user(1)
    for _ in range(count):
        book = Book.objects.create(
            title=fake.sentence(nb_words=4),
            author=fake.name(),
            published_date=timezone.now(),
            owner=random.choice(owners)
        )
        books.append(book)
    return books
