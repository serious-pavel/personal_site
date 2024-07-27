from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.posts, name='posts'),
    path('posts/<str:slug>', views.post, name='post'),
    path('posts/read-later/', views.read_later, name='read_later')
]
