from rest_framework import viewsets, permissions, filters, generics
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Like
from notifications.models import Notification
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        following_users = user.following.all()  # قائمة المستخدمين الذين يتابعهم
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

# View لعمل Like
class LikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)

        # تحقق إذا كان المستخدم قد عمل like بالفعل
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if created:
            # أنشئ Notification للكاتب
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target=post
            )
            return Response({"message": "Post liked"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "You already liked this post"}, status=status.HTTP_200_OK)


# View لعمل Unlike
class UnlikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        like = Like.objects.filter(user=request.user, post=post).first()

        if like:
            like.delete()
            return Response({"message": "Post unliked"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "You haven't liked this post"}, status=status.HTTP_400_BAD_REQUEST)