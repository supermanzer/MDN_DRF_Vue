from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from catalog.models import Book, Author, BookInstance

from .serializers import BookSerializer, InstanceSerializer, AuthorSerializer


class BookViewset(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication]


class AuthorViewset(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication]



class InstanceViewset(ModelViewSet):
    queryset = BookInstance.objects.all()
    serializer_class = InstanceSerializer
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication]



class CustomAuthToken(ObtainAuthToken):
    """Creating a Custom Authentication Token view

    This is used to pass more data to the requesting front-end
    """

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user': {
                'first_name': user.first_name,
                'last_name': user.last_name,
                'id': user.id,
                'is_staff': user.is_staff
            }
        })

