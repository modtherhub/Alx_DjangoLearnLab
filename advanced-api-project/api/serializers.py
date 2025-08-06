from rest_framework import serializers
from .models import Author, Book
import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer للكتاب يحتوي على جميع الحقول.
    ويشمل تحقق مخصص لضمان أن سنة النشر ليست في المستقبل.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer للمؤلف يشمل الحقل name,
    ويحتوي أيضا على قائمة كتب المؤلف بشكل متداخل.
    """
    books = BookSerializer(many=True, read_only=True)  # related_name = 'books'

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
