import os
import sys
import django

# ✅ Add project root to Python path manually so imports work from any folder
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')

django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # Query all books by a specific author
    try:
        author = Author.objects.get(name="J.K. Rowling")
        books_by_author = author.books.all()
        print(f"📚 Books by {author.name}: {[book.title for book in books_by_author]}")
    except Author.DoesNotExist:
        print("❌ Author 'J.K. Rowling' not found.")

    # List all books in a library
    try:
        library = Library.objects.get(name="Central Library")
        books_in_library = library.books.all()
        print(f"🏛️ Books in {library.name}: {[book.title for book in books_in_library]}")
    except Library.DoesNotExist:
        print("❌ Library 'Central Library' not found.")

    # Retrieve the librarian for a library
    try:
        librarian = library.librarian  # assumes `library` from above
        print(f"👨‍🏫 Librarian of {library.name}: {librarian.name}")
    except Exception as e:
        print("❌ Could not retrieve librarian:", e)

if __name__ == "__main__":
    run_queries()
