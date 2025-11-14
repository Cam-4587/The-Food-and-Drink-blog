from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.shortcuts import redirect
from django.views import generic
from .models import Post
from .forms import CreateBlogPost

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

def editpost(request, slug):
    """ Edits Users blog post and redirects user back to their blog post """
    post = get_object_or_404(Post, slug=slug)

    # Check if the current user is the author of the post
    if post.author != request.user:
        messages.error(
            request, "You do not have permission to edit this post.")
        return redirect('home')

    if request.method == 'POST':
        form = CreateBlogPost(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateBlogPost(instance=post)
    return render(request, 'edit_post.html', {'form': form, 'post': post})

def contact(request):
        return render(request, "contact.html") 