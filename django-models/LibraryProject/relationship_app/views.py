from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library    # ✅ <- This is required for the check
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile



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

# Task 03

def role_required(role):
    def decorator(view_func):
        return login_required(user_passes_test(lambda u: u.userprofile.role == role)(view_func))
    return decorator

@role_required('Admin')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@role_required('Librarian')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@role_required('Member')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')