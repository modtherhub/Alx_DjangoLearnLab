from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('books/', views.list_books, name='list_books'),                    # FBV for listing all books
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # CBV for library details
]
