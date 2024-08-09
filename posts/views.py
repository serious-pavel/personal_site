from django.shortcuts import render, redirect
from .models import Post, Comment
from django.shortcuts import get_object_or_404
from .forms import CommentForm

# Create your views here.


def index(request):
    recent_blog_posts = Post.objects.all().order_by('-date_modified')[:3]
    return render(request, 'posts/index.html', context={'recent_blog_posts': recent_blog_posts})


def posts(request):
    blog_posts = Post.objects.all()
    return render(request, 'posts/posts.html', context={'blog_posts': blog_posts})


def post(request, slug):
    blog_post = get_object_or_404(Post, slug=slug)
    comment = Comment.objects.create(post=blog_post)
    form = CommentForm(request.POST or None, instance=comment)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('post', slug=slug)

    return render(request, 'posts/post.html', {'blog_post': blog_post, 'form': form, })


def read_later(request):
    return render(request, 'posts/read_later.html')
