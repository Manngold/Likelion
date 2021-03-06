from django.shortcuts import render,redirect
from blog.models import Blog
from django.utils import timezone
# Create your views here.

def index(request):
    blogs = Blog.objects
    return render(request, 'index.html', {'blogs': blogs})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()

    return redirect('index')

