import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def queries():
    author = Author.objects.get(name="Chinua Achebe")
    print("Books by Chinua Achebe:")
    for book in Book.objects.filter(author=author):
        print(book.title)

    library = Library.objects.get(name="Main Library")
    print("\nBooks in Main Library:")
    for book in library.books.all():
        print(book.title)

    librarian = Librarian.objects.get(library=library)
    print(f"\nLibrarian for Main Library: {librarian.name}")

if __name__ == "__main__":
    queries()
