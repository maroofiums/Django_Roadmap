from faker import Faker
from .models import Book
import random
from datetime import datetime

fake = Faker()

def generate_fake_books(n=10):
    """
    Generates 'n' fake Book objects and saves them to the database.
    """
    for _ in range(n):
        title = fake.sentence(nb_words=4)        # Fake title
        author = fake.name()                      # Fake author
        published_date = fake.date_between(start_date='-10y', end_date='today')
        
        Book.objects.create(
            title=title,
            author=author,
            published_date=published_date
        )

    print(f"{n} fake books created!")
