"""Catalog app URL configuration

This file defines the URLS used to access REST API endpoints related to the catalog app.  It
exposes the API router to allow extending the regisrtry of the root router
"""
from rest_framework.routers import SimpleRouter
from .views import AuthorViewSet, BookViewSet, BookInstanceViewSet, GenreViewset

router = SimpleRouter()

router.register('authors', AuthorViewSet)
router.register('books', BookViewSet),
router.register('book_instances', BookInstanceViewSet)
router.register('genres', GenreViewset)
