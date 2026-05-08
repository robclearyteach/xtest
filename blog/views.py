from django.shortcuts import render
from django.http import HttpResponse
from . models import Post
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView              # ADDED                          
)

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin    



# ADD a class-based view for delete...
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): 
    model = Post
    success_url = "/blog"               # ADD a redirect back to the 'Home' view after successfully deleting a Post

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
    
# ADD a class-based view for update 
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):          # UPDATED: Inherits above now.
    model = Post
    fields = ['title', 'content']
     
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    #Added 'test_func':  check the request to .../update is from the post.author 
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostCreateView(LoginRequiredMixin,CreateView):        # ADDED LoginRequiredMixin
    model = Post
    fields = ['title', 'content']  
    #Override form_valid() method 
    def form_valid(self, form):
        form.instance.author = self.request.user    
        return super().form_valid(form)             


class PostDetailView(DetailView):
    model = Post  
    
    
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' 
    context_object_name = 'posts'       
    ordering = ['-date_posted']         


#   Older function based views below 

def home(request):                  # NOT USED: PostListView above replaced this
    context_dict={
        'posts': Post.objects.all(),
        'title': 'rob-title'
    }
    return render(request, 'blog/home.html', context_dict)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})