from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.edit import CreateView
from .models import BlogPost, Profile
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic import TemplateView
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm
from .forms import UserForm, ProfileForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import logout





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

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('edit_profile')
    template_name = 'registration/signup.html'

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('homepage')  # change 'profile' to the name of the URL where you want to redirect after successful form submission

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        context = super(ProfileUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['user_form'] = UserForm(self.request.POST, instance=self.request.user)
        else:
            context['user_form'] = UserForm(instance=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        user_form = UserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()

        return super(ProfileUpdateView, self).post(request, *args, **kwargs)
class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('homepage')



class CustomLogoutView(LogoutView):

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, "Successfully logged out")
        return redirect('homepage')  # Redirect to homepage


# class MyProtectedView(LoginRequiredMixin, TemplateView):
#     template_name = 'my_template.html'
#     login_url = 'login'  # Redirect to this URL if the user is not authenticated

#----------------------------------------------------
# CRUD for posts/blogs
class BlogPostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    fields = ['title', 'content']  # Add your model fields here
    template_name = 'blog/blog_create.html'
    login_url = 'login'  # Redirect to this URL if the user is not authenticated
    success_url = reverse_lazy('homepage')  # Use reverse_lazy instead of a hardcoded URL

    def form_valid(self, form):
        # Assign the logged-in user's profile to the blog post before saving it
        form.instance.profile = self.request.user.profile  # Adjust this as per your user-profile association
        return super().form_valid(form)
class BlogPostListView(LoginRequiredMixin, ListView):
    model = BlogPost
    template_name = 'blog/blog_read_listview.html'
    login_url = 'login'  # Redirect to this URL if the user is not authenticated
    context_object_name = 'objects'
class BlogPostDetailView(LoginRequiredMixin, DetailView):
    model = BlogPost
    template_name = 'blog/blog_read.html'
    login_url = 'login'  # Redirect to this URL if the user is not authenticated
    context_object_name = 'post'  # You might want to change this to something like 'post' for clarity
class BlogPostUpdateView(LoginRequiredMixin, UpdateView):
    model = BlogPost
    fields = ['title', 'content']  # add your model fields here
    template_name = 'blog/blog_update.html'
    login_url = 'login'  # Redirect to this URL if the user is not authenticated
    success_url = '/'  # Redirect to a success page upon successful update
class BlogPostDeleteView(LoginRequiredMixin, DeleteView):
    model = BlogPost
    template_name = 'blog/blog_delete.html'
    login_url = 'login'  # Redirect to this URL if the user is not authenticated
    success_url = reverse_lazy('read_class')  # Redirect to the list view upon successful deletion

