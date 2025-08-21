from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerializer
from .models import CustomUser
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

# Register view
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = serializer.validated_data['token']
        return Response({"user": user.username, "token": token})