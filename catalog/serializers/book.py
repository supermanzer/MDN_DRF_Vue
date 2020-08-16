from rest_framework.serializers import ModelSerializer
from catalog.models import Book
from .instance import InstanceSerializer


class BookSerializer(ModelSerializer):
    copies = InstanceSerializer(many=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'summary',
                  'isbn', 'get_genres', 'copies']
