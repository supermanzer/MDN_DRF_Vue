from .models import Genre, Book, Author, BookInstance
from rest_framework import serializers


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = ['url', 'id', 'name', 'books']
        search_fields = ['name']


class BookSerializer(serializers.HyperlinkedModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['url', 'title', 'display_author',
                  'author', 'genres', 'summary', 'isbn']
        search_fields = ['title', 'author', 'genre', 'isbn']


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['url', 'last_name', 'first_name',
                  'date_of_birth', 'date_of_death', 'books']
        search_fields = ['last_name', 'first_name',
                         'date_of_birth', 'date_of_death']


class BookInstanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookInstance
        fields = ['url', 'id', 'display_title', 'book',
                  'get_status_display', 'due_back']
