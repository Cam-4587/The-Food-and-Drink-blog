from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

# Create your views here.

def home(request):
    return render(request, "home.html") 

# def blog(request):
#     return render(request, "blog.html") 

class blog(generic.ListView):
    """ Display published blog posts on the home page"""
    queryset = Post.objects.filter(status=1)
    template_name = "blog.html"


def post_blog(request, slug):
    """ Display individual blog post with comment section at the bottom"""
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)

    context = {
        "post": post,
    }

    return render(
        request,
        "post_blog.html",
        context
    )

def contact(request):
    return render(request, "contact.html") 