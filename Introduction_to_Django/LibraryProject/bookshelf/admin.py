from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to display
    list_filter = ('publication_year', 'author')            # Filters sidebar
    search_fields = ('title', 'author')                      # Search box


admin.site.register(Book)