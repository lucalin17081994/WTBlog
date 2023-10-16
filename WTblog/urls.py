"""
URL configuration for WTblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from blog.views import BlogPostCreateView, BlogPostListView, BlogPostDetailView, BlogPostUpdateView, BlogPostDeleteView, HomePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('blog_create/', BlogPostCreateView, name='create'),  # Function-based view example
    # path('blog_read/', read_view, name='read'),
    # path('blog_update/<int:pk>/', update_view, name='update'),
    # path('blog_delete/<int:pk>/', delete_view, name='delete'),
    path('', HomePageView.as_view(), name='homepage'),
    # path('', include('home.urls')),  # new
    path('blog_create/', BlogPostCreateView.as_view(), name='create_class'),  # Class-based view example
    path('blog_read/<int:pk>/', BlogPostDetailView.as_view(), name='blog_detail'),
    path('blog_read/', BlogPostListView.as_view(), name='read_class'),
    path('blog_update/<int:pk>/', BlogPostUpdateView.as_view(), name='update_class'),
    path('blog_delete/<int:pk>/', BlogPostDeleteView.as_view(), name='delete_class'),
    
]

