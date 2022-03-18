
from ast import Del, Delete
from django.urls import reverse
from django.shortcuts import render, get_object_or_404

from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect

# Create your views here.
# Using bootswatch litera theme
# Using bootswatch litera theme

class HomeView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-date"]

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post-detail.html"
    context_object_name = "post"

class PostCreateView(CreateView):
    model = Post
    template_name = "blog/post-create.html"
    fields = ["title", "excerpt", "content", "tags"]
    success_url = "/posts"
    
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        
class PostUpdateView(UpdateView):
    model = Post
    template_name = "blog/post-create.html"
    fields = ["title", "excerpt", "content", "tags"]
    success_url = "/posts"


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # def test_func(self):
    #     post = self.get_object()
    #     if self.request.user == post.author:
    #         return True
    #     return False


# "**/templates/*": "django-txt",
class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post-delete-confirmation.html"
    success_url = "/posts"
