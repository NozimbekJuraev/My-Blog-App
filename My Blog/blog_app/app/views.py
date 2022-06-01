from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post 

# Create your views here.

class HomePage(ListView):
    model = Post
    template_name = 'home.html'


class PostDetailed(DetailView):
    model = Post
    template_name = 'post_detailed.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'new_post.html'
    fields = ['title', 'author','text']

class Blogupdate(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'text']

class BlogDelete(DeleteView):
    modeL = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')