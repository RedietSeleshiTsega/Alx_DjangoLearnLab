from django import forms
from .models import Book

class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, strip=True)

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'isbn']