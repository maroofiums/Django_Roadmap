import random
from faker import Faker
from django.contrib.auth.models import User
from .models import Post

fake = Faker()

def generate_fake_users(n=5):
    for _ in range(n):
        username = fake.user_name()
        email = fake.email()
        password = "password123"

        # Avoid duplicate users
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, email=email, password=password)
            print(f"✅ Created user: {username}")

def generate_fake_posts(n=20):
    users = list(User.objects.all())
    if not users:
        print("⚠️ No users found. First generate fake users.")
        return

    for _ in range(n):
        user = random.choice(users)
        title = fake.sentence(nb_words=6)
        content = fake.paragraph(nb_sentences=5)

        Post.objects.create(user=user, title=title, content=content)

    print(f"✅ Created {n} fake posts.")
