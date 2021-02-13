from django.urls import path, include
from .views import posts_list, post_detail, post_write, comment_write, post_like

urlpatterns = [
    path('post/', posts_list, name='posts_list'),
    path('post/<int:post_id>', post_detail, name='post_detail'),
    path('post/write', post_write, name='post_write'),
    path('comment/write', comment_write, name='comment_write'),
    path('post_like/', post_like, name='post_like'),
]