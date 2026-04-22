from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True, default="")
    birth_year = models.IntegerField(null=True, blank=True)
    nationality = models.CharField(max_length=100, blank=True, default="")

    def __str__(self):
        return self.name