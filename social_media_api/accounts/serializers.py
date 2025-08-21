from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password
from rest_framework.authtoken.models import Token

# Serializer لتسجيل المستخدم
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)  # لتأكيد الباسورد

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'password2', 'bio', 'profile_picture')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = CustomUser.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

# Serializer لتسجيل الدخول
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        from django.contrib.auth import authenticate
        user = authenticate(**data)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return {"user": user, "token": token.key}
        raise serializers.ValidationError("Invalid credentials")
