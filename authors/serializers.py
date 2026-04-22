from rest_framework import serializers
from .models import Author
from books.models import Book

class BookSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'published_year', 'theme']

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSummarySerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'bio', 'birth_year', 'nationality', 'books']