# books/views.py

from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet automatically provides:
    list, create, retrieve, update, destroy actions.
    """
    queryset = Book.objects.all()          # which records to expose
    serializer_class = BookSerializer      # how to convert them to JSON