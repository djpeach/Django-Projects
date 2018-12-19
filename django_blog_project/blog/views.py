from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth import mixins
from django.contrib.auth.models import User
from django.views import generic

class PostCreateView(mixins.LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostListView(generic.ListView):
    model = Post
    ordering = ['-date_posted']
    paginate_by = 2
    

class UserPostListView(generic.ListView):
    template_name = 'blog/user_post_list.html'
    model = Post
    ordering = ['-date_posted']
    paginate_by = 2
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
    
    
class PostDetailView(generic.DetailView):
    model = Post
    
    
class PostUpdateView(mixins.LoginRequiredMixin, mixins.UserPassesTestMixin, generic.UpdateView):
    model = Post
    fields = ['title', 'content']
    
    def test_func(self):
        return self.request.user == self.get_object().author


class PostDeleteView(mixins.LoginRequiredMixin, mixins.UserPassesTestMixin, generic.DeleteView):
    model = Post
    success_url = '/blog/'
    
    def test_func(self):
        return self.request.user == self.get_object().author

