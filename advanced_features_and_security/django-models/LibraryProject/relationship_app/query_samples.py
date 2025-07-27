import os
import sys
import django

# Setup Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # Query all books by a specific author
    author_name = "J.K. Rowling"
    try:
        author = Author.objects.get(name=author_name)
        books_by_author = Book.objects.filter(author=author)  # ✅ Match expected syntax
        print(f"📚 Books by {author.name}: {[book.title for book in books_by_author]}")
    except Author.DoesNotExist:
        print(f"❌ Author '{author_name}' not found.")

    # List all books in a library
    library_name = "Central Library"
    try:
        library = Library.objects.get(name=library_name)
        books_in_library = library.books.all()
        print(f"🏛️ Books in {library.name}: {[book.title for book in books_in_library]}")
    except Library.DoesNotExist:
        print(f"❌ Library '{library_name}' not found.")
        library = None

    # Retrieve the librarian for a library
    try:
        if library:
            librarian = Librarian.objects.get(library=library)  # ✅ Required syntax
            print(f"👨‍🏫 Librarian of {library.name}: {librarian.name}")
    except Librarian.DoesNotExist:
            print(f"❌ Librarian for '{library_name}' not found.")

if __name__ == "__main__":
    run_queries()
