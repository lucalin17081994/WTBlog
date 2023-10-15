from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView
from .models import BlogPost

class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ['username', 'title', 'content']  # add your model fields here
    template_name = 'blog_create.html'
    success_url = '/blog_read/'  # Redirect to a success page upon successful creation

from django.views.generic import ListView

class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog_read.html'
    context_object_name = 'objects'

from django.views.generic.edit import UpdateView

class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ['username', 'title', 'content']  # add your model fields here
    template_name = 'blog_update.html'
    success_url = '/blog_read/'  # Redirect to a success page upon successful update


from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('read_class')  # Redirect to the list view upon successful deletion

