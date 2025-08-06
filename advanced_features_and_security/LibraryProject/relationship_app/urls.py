from django.urls import path
from bookshelf.views import (
    list_books,
    LibraryDetailView,
    login_view,
    logout_view,
    register_view,
    home,
    admin_view,
    librarian_view,
    member_view,
    add_book,
    edit_book, 
    delete_book
)

urlpatterns = [
    path('', home, name='home'),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # auth views
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),

    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),

    path('books/add/', add_book, name='add_book'),
    path('books/edit/<int:pk>/', edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', delete_book, name='delete_book'),

]
