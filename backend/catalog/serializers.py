from .models import Genre, Book, Author, BookInstance
from rest_framework import serializers


class BooKListSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'url', 'title', 'author']


class AuthorListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'url', 'fist_name', 'last_name',
                  'date_of_birth', 'date_of_death']


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = ['url', 'id', 'name', 'books']
        search_fields = ['name']
        depth = 1


class BookInstanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookInstance
        fields = ['id', 'url', 'display_title', 'book',
                  'get_status_display', 'due_back']


class BookDetailSerializer(serializers.HyperlinkedModelSerializer):
    # genres = serializers.StringRelatedField(many=True, read_only=True)
    copies = BookInstanceSerializer(many=True, read_only=True)
    # author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'url', 'title',
                  'author', 'genres', 'summary', 'isbn', 'copies', 'header_image']
        search_fields = ['title', 'author', 'genre', 'isbn']
        depth = 1


class AuthorDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'url', 'last_name', 'first_name',
                  'date_of_birth', 'date_of_death', 'books']
        search_fields = ['last_name', 'first_name',
                         'date_of_birth', 'date_of_death']
        depth = 1
