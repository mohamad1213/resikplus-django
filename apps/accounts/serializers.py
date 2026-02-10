from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # attrs mengandung 'email' dan 'password'
        data = super().validate(attrs)

        # Tentukan role: jika is_staff atau is_superuser maka admin
        user = self.user
        # Tambahkan ke response JSON agar dibaca res.data.user di React
        data['user'] = {
            'id': self.user.id,
            'email': self.user.email,
            'is_staff': user.is_staff,
            'is_superuser': user.is_superuser,
            'full_name': self.user.get_full_name
        }
        return data

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, max_length=128, min_length=8, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, max_length=128, min_length=8, write_only=True)  
    class Meta:
        model = User
        fields =  ['email','first_name', 'last_name', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("Passwords do not match")
        return attrs
    def create(self, validated_data):
        user = User.objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=validated_data['password']
        )   
        return user
    
class VerifyOTPSerializer(serializers.Serializer):

    email = serializers.EmailField()
    otp = serializers.CharField()


class UserCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'data_joined']
        read_only_fields = ['data_joined']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = super().create(validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user
        
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

