from rest_framework.serializers import ModelSerializer, StringRelatedField

from catalog.models import Author


class AuthorSerializer(ModelSerializer):

    class Meta:
        model = Author
        fields = ['last_name', 'first_name',
                  'date_of_birth', 'date_of_death', 'books']
