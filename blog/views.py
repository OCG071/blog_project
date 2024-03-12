from django.shortcuts import render,get_object_or_404
from django.http import Http404
from .models import Post

def post_list(request):
    posts = Post.publish.all()
    return render(request, 'blog/post/list.html',{'post':posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id = id, status = Post.Status.PUBLISH)
    return render(request, 'blog/post/detail.html',{'post':post})
# Create your views here.
