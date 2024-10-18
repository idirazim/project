from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet, GenreViewSet

router = DefaultRouter()
router.register('authors', AuthorViewSet, basename='author-api')
router.register('books', BookViewSet, basename='book-api')
router.register('genres', GenreViewSet, basename='genre-api')

urlpatterns = []
urlpatterns += router.urls
