from django.shortcuts import render
from .models import Post

def home(req):
    context = {
        'posts': Post.objects.all()
    }
    return render(req, 'forum/index.html', context)
