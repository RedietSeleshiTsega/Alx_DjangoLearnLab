from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITestCase(APITestCase):
    def setUp(self):
        """Set up test data and client"""
        self.client = APIClient()
        
      
        self.admin = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='testpass123'
        )
        self.user = User.objects.create_user(
            username='testuser',
            email='user@example.com',
            password='testpass123'
        )
        
      
        self.author = Author.objects.create(name='J.R.R. Tolkien')
        
        
        self.book1 = Book.objects.create(
            title='The Hobbit',
            publication_year=1937,
            author=self.author,
            created_by=self.user
        )
        self.book2 = Book.objects.create(
            title='The Lord of the Rings',
            publication_year=1954,
            author=self.author,
            created_by=self.admin
        )