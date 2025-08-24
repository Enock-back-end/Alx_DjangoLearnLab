from django.urls import path
from . import views
from .views import RegisterView, LoginView, ProfileView
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView, ProfileView
from .views import RegisterView, LoginView, ProfileView, FollowUserView, UnfollowUserView
from .views import FollowUserView, UnfollowUserView

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", obtain_auth_token, name="login"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("profile/", ProfileView.as_view(), name="profile"),
        path("register/", RegisterView.as_view(), name="register"),
    path("login/", obtain_auth_token, name="login"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),

   
   
]

