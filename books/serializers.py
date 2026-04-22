# books/serializers.py

from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book                    # which model to serialize
        fields = '__all__'              # include all fields
        # or use: fields = ['id', 'title', 'author']  to pick specific ones