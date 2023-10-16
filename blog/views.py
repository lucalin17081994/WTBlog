from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.edit import CreateView
from .models import BlogPost
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic import TemplateView
from django.views.generic import DetailView
from django.urls import reverse_lazy


class HomePageView(ListView):
    # template_name = 'home/index.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['posts'] = BlogPost.objects.all()[:10]  # Adjust the query as needed
    #     return context
    model = BlogPost
    template_name = 'home/index.html'  
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        
        return BlogPost.objects.all()

# CRUD for posts/blogs
class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ['username', 'title', 'content']  # add your model fields here
    template_name = 'blog_create.html'
    success_url = '/'  # Redirect to a success page upon successful creation
class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog_read_listview.html'
    context_object_name = 'objects'
class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog_read.html'
    context_object_name = 'post'  # You might want to change this to something like 'post' for clarity
class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ['username', 'title', 'content']  # add your model fields here
    template_name = 'blog_update.html'
    success_url = '/'  # Redirect to a success page upon successful update
class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('read_class')  # Redirect to the list view upon successful deletion

