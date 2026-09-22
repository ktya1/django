from django.urls import path

from users.views import login_view


urlpatterns = [
    path('users/login/', login_view, name='users-login'),
#     path('users/register/', ..., name='users-register'),
#     path('users/profile/', ..., name='users-profile'),
#     path('users/logout/', ..., name='users-logout'),
]

