from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.posts, name='posts'),
    path('posts_old/<str:article_slug>', views.post_old, name='post_old'),
    path('posts/<str:slug>', views.post, name='post'),
]
