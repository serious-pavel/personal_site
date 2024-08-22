from django.urls import path
from . import views
from .views import IndexListView, PostsListView, ReadLaterListView, PostView

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('posts/', PostsListView.as_view(), name='posts'),
    path('posts/read-later/', ReadLaterListView.as_view(), name='read_later'),
    path('posts/<str:slug>', PostView.as_view(), name='post'),
]
