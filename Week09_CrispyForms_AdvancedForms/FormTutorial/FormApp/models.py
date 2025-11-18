from django.db import models
from django.urls import reverse

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # After creating/updating, redirect to detail view
        return reverse('book-detail', kwargs={'pk': self.pk})
