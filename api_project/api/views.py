from rest_framework import generics, viewsets  # Add these imports
from .models import Book
from .serializers import BookSerializer

# Keep your existing BookList view
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Add ViewSet
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer