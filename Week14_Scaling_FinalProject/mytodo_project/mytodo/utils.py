from django.core.cache import cache
from faker import Faker
from .models import Post

faker = Faker()

def create_fake_posts(n=10):
    for _ in range(n):
        Post.objects.create(
            title=faker.sentence(),
            content=faker.text()
        )
    
    print(f"Created {n} fake posts.")
    
def clear_posts():
    Post.objects.all().delete()
    print("All posts have been deleted.")
    
    
        

def get_all_todos():
    todos = cache.get("all_todos")
    if not todos:
        todos = list(Post.objects.all())
        cache.set("all_todos", todos, timeout=300)  
    return todos
