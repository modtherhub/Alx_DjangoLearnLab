from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library    # ✅ <- This is required for the check
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.http import HttpResponse


# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view for Library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto login after registration
            return redirect('home')  # Redirect to home or wherever
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

def home(request):
    return HttpResponse("<h1>Welcome to the Library App!</h1><p><a href='/books/'>View Books</a></p>")