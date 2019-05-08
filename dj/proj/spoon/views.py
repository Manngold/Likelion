from django.shortcuts import render,redirect, get_object_or_404
import random
from spoon.models import Post
from django.utils import timezone
# Create your views here.

def index(request):
    return render(request, 'index.html')

def result(request):
    name = request.GET['name']
    spoon = [1, 2, 3, 4, 5]
    ability = ['ugly', 'clever', 'godness', 'handsome', 'idot']
    random.shuffle(spoon)
    random.shuffle(ability)
    return render(request, 'result.html', {'name': name, 'spoon':spoon, 'ability': ability})

def post(request):
    posts = Post.objects
    return render(request, 'post.html', {'posts': posts})

def new(request):
    return render(request, 'new.html')

def create(request):
    post = Post()
    post.title = request.GET['title']
    post.body = request.GET['body']
    post.pubDay = timezone.datetime.now()
    post.save()

    return redirect('post')

def update_page(request, post_id):
    updatePost = get_object_or_404(Post, pk=post_id)
    return render(request, 'update_page.html', {'post': updatePost})

def update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.title = request.GET['title']
    post.body = request.GET['body']
    post.pubDay = timezone.datetime.now()
    post.save()
    return redirect('post')

def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('post')