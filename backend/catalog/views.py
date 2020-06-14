from .models import Genre, Author, Book, BookInstance
from rest_framework import viewsets

from . import serializers


class GenreViewset(viewsets.ModelViewSet):
    queryset = Genre.objects.all().prefetch_related('books')
    serializer_class = serializers.GenreSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()  # .prefetch_related('books')
    serializer_class = serializers.AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.select_related(
        'author').all().prefetch_related('copies')
    serializer_class = serializers.BookSerializer


class BookInstanceViewSet(viewsets.ModelViewSet):
    queryset = BookInstance.objects.select_related('book').all()
    serializer_class = serializers.BookInstanceSerializer
