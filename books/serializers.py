# books/serializers.py

from rest_framework import serializers
from authors.models import Author
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.name', read_only=True)

    class Meta:
        model = Book                    # which model to serialize
        fields = '__all__'              # include all fields
        # or use: fields = ['id', 'title', 'author']  to pick specific ones