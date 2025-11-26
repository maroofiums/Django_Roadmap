from faker import Faker
from .models import Post

fake = Faker()

def generate_fake_posts(n=10):
    for _ in range(n):
        Post.objects.create(
            title=fake.sentence(),
            content=fake.paragraph(),
        )
    return f"{n} fake posts created!"
