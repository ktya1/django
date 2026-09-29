from django.urls import path

from posts.views import create_post, list_posts, read_post


urlpatterns = [
    path('posts/create/', create_post, name='create-post'),
    path('posts/list/',list_posts, name = 'list-posts' ),
    path('posts/<int:post_id>/',read_post , name='read-post')
]

