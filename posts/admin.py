from django.contrib import admin
from .models import Post, Author, Tag, Comment


# Register your models here.
# class AuthorAdmin(admin.ModelAdmin):
#

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_filter = ['last_name', 'first_name']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title', 'author', 'date_created']
    list_filter = ['author', 'tags', 'date_created']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    # exclude = ('post',)
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'comment_author', 'date_created']
    list_filter = ['post', 'comment_author', 'date_created']
