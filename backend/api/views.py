from django.shortcuts import render
from rest_framework import generics,permissions
from .models import Task
from .serializers import TaskSerializer,UserSerializer,EmailTokenObtainPairSerializer
# from django.contrib.auth.models import User
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.



# class CreateUserView(generics.CreateAPIView):
#     queryset=User.objects.all()
#     serializer_class=UserSerializer
#     permission_classes=[AllowAny]

class createUserView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[permissions.AllowAny]

class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class=TaskSerializer
    permission_classes=[permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        

class TaskRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=TaskSerializer
    permission_classes=[permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
    
class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class=EmailTokenObtainPairSerializer
    
