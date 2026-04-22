# books/models.py

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)       # text, max 200 chars
    author = models.CharField(max_length=100)
    published_year = models.IntegerField()
    isbn = models.CharField(max_length=13, unique=True)  # unique = no duplicates
    created_at = models.DateTimeField(auto_now_add=True) # set automatically on create

    def __str__(self):
        return f"{self.title} by {self.author}"    # how the object prints