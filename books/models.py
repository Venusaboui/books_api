# books/models.py

from django.db import models
from authors.models import Author

class Book(models.Model):
    title = models.CharField(max_length=200)  
    theme = models.CharField(max_length=100, default="General")    # text, max 200 chars
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    published_year = models.IntegerField()
    isbn = models.CharField(max_length=13, unique=True)  # unique = no duplicates
    created_at = models.DateTimeField(auto_now_add=True) # set automatically on create

    def __str__(self):
        return f"{self.title} by {self.author}"    # how the object prints