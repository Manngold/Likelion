from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import Blog
from django.utils import timezone
# Create your views here.

def index(request):
    blogs = Blog.objects
    return render(request, 'index.html', {'blogs': blogs})

def new(request):
    return render(request, 'new.html')

def create(request):
    post = Blog()
    post.title = request.GET['title']
    post.body = request.GET['body']
    post.pubDay = timezone.datetime.now()
    post.save()
    return redirect('index')

def updatePage(request, post_id):
    updatePage = get_object_or_404(Blog, pk=post_id)
    return render(request, 'updatePage.html', {'post': updatePage})

def update(request, post_id):
    post = get_object_or_404(Blog, pk=post_id)
    post.title = request.GET['title']
    post.body = request.GET['body']
    post.pubDay = timezone.datetime.now()
    post.save()
    return redirect('index')

def delete(request, post_id):
    post = get_object_or_404(Blog, pk=post_id)
    post.delete()
    return redirect('index')