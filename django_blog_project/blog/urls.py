"""django_blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""  
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'blog'
urlpatterns = [

    # Post urls
    path('new/', views.PostCreateView.as_view(), name='create'),
    path('', views.PostListView.as_view(), name='read-list'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='read-detail'),
    path('<int:pk>/update', views.PostUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', views.PostDeleteView.as_view(), name='delete'),


    # Filtered Post urls
    path('user/<str:username>', views.UserPostListView.as_view(), name='user-read-list'),
]
