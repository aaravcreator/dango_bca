from django.shortcuts import render
from .models import Blog
# Create your views here.
def blog_list(request):
    blogs = Blog.objects.all()
    print(blogs)
    context = {
        'blog_list':blogs
    }
    return render(request,'blog/blog_section.html',context)

def blog_detail(request,id):
    print(id)
    blog = Blog.objects.get(id=id)
    
    context = {
        'blog':blog
    }
    return render(request,'blog/blog_detail.html',context)