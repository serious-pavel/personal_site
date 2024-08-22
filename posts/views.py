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


def read_later(request):
    blog_posts = Post.objects.filter(id__in=request.session.get("read_later_posts", []))
    return render(request, 'posts/posts.html', context={'blog_posts': blog_posts, 'header': 'Read Later'})


def post(request, slug):
    blog_post = get_object_or_404(Post, slug=slug)
    comment = Comment(post=blog_post)
    form = CommentForm(request.POST or None, instance=comment)

    read_later_posts = request.session.get("read_later_posts", [])

    if request.method == 'POST':
        remove_id = request.POST.get('remove_id')
        add_id = request.POST.get('add_id')

        if add_id:
            read_later_posts.append(add_id)
            request.session['read_later_posts'] = read_later_posts

        if remove_id:
            read_later_posts.remove(remove_id)
            request.session['read_later_posts'] = read_later_posts

        if form.is_valid():
            form.save()

        return redirect('post', slug=slug)

    return render(request, 'posts/post.html', {'blog_post': blog_post, 'form': form, })

