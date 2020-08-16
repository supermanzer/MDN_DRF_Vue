"""URL Configuration for Catalog App
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewset, BookViewset, InstanceViewset, CustomAuthToken

# Defining a custom router for DRF
router = DefaultRouter()
router.register('books', BookViewset)
router.register('copies', InstanceViewset)
router.register('authors', AuthorViewset)

urlpatterns = [
    path('', include(router.urls)),
]


# Authetnication
urlpatterns += [
    path('auth/get-token-user', CustomAuthToken.as_view(), name='get-token')
]
