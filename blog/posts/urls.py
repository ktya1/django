from django.urls import path

from posts.views import create_post


urlpatterns = [
    path('posts/create/', create_post, name='create-post')
]