from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library

# Function-based view: list all books with their authors as plain text
def list_books(request):
    books = Book.objects.all()  # important for the check
    output = "\n".join(f"{book.title} by {book.author.name}" for book in books)
    return HttpResponse(output, content_type="text/plain")

# Class-based DetailView: show a specific library and its books (using template)
class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"
