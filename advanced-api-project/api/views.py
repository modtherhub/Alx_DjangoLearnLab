from rest_framework import generics, permissions, filters
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

# عرض جميع الكتب (List)
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # للجميع إمكانية القراءة

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['title', 'author__name', 'publication_year']

    # البحث
    search_fields = ['title', 'author__name']

    # الترتيب
    ordering_fields = ['title', 'publication_year']

# عرض كتاب واحد حسب الـ pk (Retrieve)
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # للجميع إمكانية القراءة

# إنشاء كتاب جديد (Create)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # فقط للمستخدمين المسجلين

# تحديث كتاب موجود (Update)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # فقط للمستخدمين المسجلين

# حذف كتاب (Delete)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # فقط للمستخدمين المسجلين
