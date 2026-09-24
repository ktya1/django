from django.urls import path

from users.views import login_view,logout_view, profile_view


urlpatterns = [
    path('users/login/', login_view, name='users-login'),
#     path('users/register/', ..., name='users-register'),
    path('users/profile/', profile_view,  name='users-profile'),
    path('users/logout/', logout_view, name='users-logout')
]

