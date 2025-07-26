from django.contrib import admin
from django.urls import path,include
from .views import createUserView,TaskListCreateView,TaskRetrieveUpdateDeleteView




urlpatterns = [
    path('user/register',createUserView.as_view(),name='register'),
    path('tasks/',TaskListCreateView.as_view(),name="tasks_list"),
    path('tasks/update/<int:pk>/',TaskRetrieveUpdateDeleteView.as_view(),name='update')
    
]


