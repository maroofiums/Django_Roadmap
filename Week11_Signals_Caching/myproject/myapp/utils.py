from faker import Faker
from .models import Post
from django.contrib.auth.models import User

fake = Faker()

def generate_fake_users(n=5):
    """Generate n fake users. Profiles auto-create via signals."""
    for _ in range(n):
        username = fake.user_name()
        email = fake.email()
        password = "password123"
        
        User.objects.create_user(username=username, email=email, password=password)
    
    print(f"✅ Created {n} fake users (profiles auto-created).")

def generate_fake_posts(n=10):
    """Generate n fake posts for existing users."""
    users = list(User.objects.all())
    if not users:
        print("⚠️ No users exist. Create users first.")
        return

    for _ in range(n):
        Post.objects.create(
            title=fake.sentence(nb_words=6),
            content=fake.paragraph(nb_sentences=5),
            # If Post has user: user=random.choice(users)
        )
    
    print(f"✅ Created {n} fake posts.")
