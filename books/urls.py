# books/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

# Router auto-generates URL patterns from a ViewSet
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
]