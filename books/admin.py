from django.contrib import admin
from .models import Book

# Register your models here.
admin.site.register(Book)  # this makes the Book model manageable via the admin interface