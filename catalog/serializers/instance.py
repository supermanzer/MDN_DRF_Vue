from rest_framework.serializers import ModelSerializer
from catalog.models import BookInstance


class InstanceSerializer(ModelSerializer):

    class Meta:
        model = BookInstance
        fields = ['book', 'imprint', 'language', 'due_back', 'status']
