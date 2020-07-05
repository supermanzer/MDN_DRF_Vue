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

    def get_serializer_class(self, detail=False):
        if detail:
            ser = serializers.AuthorDetailSerializer
        else:
            ser = serializers.AuthorListSerializer
        return ser

    def list(self, request):
        queryset = self.queryset
        serializer = self.get_serializer_class()(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        # Registering hw ofter a user looks at a particular author
        n_views = request.session.get('n_views', 0)
        request.session['n_views'] = n_views + 1
        queryset = self.queryset.prefetch_related('books')
        author = get_object_or_404(queryset, pk=pk)
        seriailizer = self.get_serializer_class(detail=True)(
            author, context={'request': request, 'n_views': n_views})
        return Response(seriailizer.data)


class BookViewSet(viewsets.ModelViewSet):

    queryset = Book.objects.select_related('author').all()

    def get_serializer_class(self, detail=False):
        if detail:  # if the request contains the id of a Book
            ser = serializers.BookDetailSerializer
        else:
            ser = serializers.BooKListSerializer
        return ser

    def list(self, request):
        queryset = self.queryset
        serializer = self.get_serializer_class()(
            queryset, many=True, context={'request': request})
        return Response(serializer.data, )

    def retrieve(self, request, pk=None):
        queryset = self.queryset.prefetch_related('copies')
        book = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer_class(detail=True)(
            book, context={'request': request})
        return Response(serializer.data)


class BookInstanceViewSet(viewsets.ModelViewSet):
    queryset = BookInstance.objects.select_related('book').all()
    serializer_class = serializers.BookInstanceSerializer
