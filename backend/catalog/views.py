from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from .models import Genre, Author, Book, BookInstance
from rest_framework import viewsets

from . import serializers


class GenreViewset(viewsets.ModelViewSet):
    queryset = Genre.objects.all().prefetch_related('books')
    serializer_class = serializers.GenreSerializer


class AuthorViewSet(viewsets.ModelViewSet):

    queryset = Author.objects.all()

    def list(self, request):
        queryset = self.queryset
        serializer = serializers.AuthorListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.queryset.prefetch_related('books')
        author = get_object_or_404(queryset, pk=pk)
        seriailizer = serializers.AuthorDetailSerializer(author)
        return Response(seriailizer.data)


class BookViewSet(viewsets.ModelViewSet):

    queryset = Book.objects.select_related('author').all()

    def list(self, request):
        queryset = self.queryset
        serializer = serializers.BookDetailSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.queryset.prefetch_related('copies')
        book = get_object_or_404(queryset, pk=pk)
        serializer = serializers.BookDetailSerializer(book)
        return Response(serializer.data)


class BookInstanceViewSet(viewsets.ModelViewSet):
    queryset = BookInstance.objects.select_related('book').all()
    serializer_class = serializers.BookInstanceSerializer
