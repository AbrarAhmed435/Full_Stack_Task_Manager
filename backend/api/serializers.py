from django.contrib.auth.models import User
from .models import Task
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate,get_user_model



class UserSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(required=True)
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['id','email','password']
        extra_kwargs={
            'email':{'required':True},   
        }
        
    def create(self,validated_data):
            username=validated_data['email'].split('@')[0]
            user=User.objects.create_user(
                username=username,
                email=validated_data['email'],
                password=validated_data['password']
            )
            return user
        
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields=['id','title','completed','created_at','updated_at']
        read_only_fields=['id','created_at','updated_at']
        

User = get_user_model()

class EmailTokenObtainPairSerializer(serializers.Serializer):
    email = serializers.EmailField(label="Enter Email") # by defautl it is Email
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid email or password")

        if not user.check_password(password):
            raise serializers.ValidationError("Invalid email or password")

        if not user.is_active:
            raise serializers.ValidationError("User is inactive")

        refresh = RefreshToken.for_user(user)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }