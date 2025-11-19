from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published_date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')  # owner field

    def __str__(self):
        return self.title
