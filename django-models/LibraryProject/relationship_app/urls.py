from django.urls import path
from .views import (
    list_books,
    add_book,
    edit_book,
    delete_book,
    login_view,
    logout_view,
    register_view,
    admin_view,
    librarian_view,
    member_view,
    LibraryDetailView
)

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:book_id>/', edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', delete_book, name='delete_book'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('admin_view/', admin_view, name='admin_view'),
    path('librarian_view/', librarian_view, name='librarian_view'),
    path('member_view/', member_view, name='member_view'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
