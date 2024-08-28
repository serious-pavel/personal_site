from django.shortcuts import render, redirect
from .models import Post, Comment
from django.shortcuts import get_object_or_404
from .forms import CommentForm
from django.views import View
from django.views.generic import ListView, DetailView

# Create your views here.


class IndexListView(ListView):
    template_name = 'posts/index.html'
    context_object_name = 'recent_blog_posts'
    queryset = Post.objects.all().order_by('-date_modified')[:3]


class PostsListView(ListView):
    template_name = 'posts/posts.html'
    context_object_name = 'blog_posts'
    model = Post  # queryset = Post.objects.all()


class ReadLaterListView(ListView):
    template_name = 'posts/posts.html'
    context_object_name = 'blog_posts'

    def get_queryset(self):
        return Post.objects.filter(id__in=self.request.session.get("read_later_posts", []))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = 'Read Later'
        return context


class PostView(View):

    def get(self, request, slug):
        blog_post = get_object_or_404(Post, slug=slug)
        form = CommentForm()

        return render(request, 'posts/post.html', {'blog_post': blog_post, 'form': form})

    def post(self, request, slug):
        read_later_posts = request.session.get("read_later_posts", [])
        remove_id = request.POST.get('remove_id')
        add_id = request.POST.get('add_id')

        if add_id:
            read_later_posts.append(int(add_id))
            request.session['read_later_posts'] = read_later_posts

        if remove_id:
            read_later_posts.remove(int(remove_id))
            request.session['read_later_posts'] = read_later_posts

        blog_post = get_object_or_404(Post, slug=slug)

        comment = Comment(post=blog_post)
        form = CommentForm(request.POST, instance=comment)

        if form.is_valid():
            form.save()

        return redirect('post', slug=slug)
