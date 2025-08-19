from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.user_profile, name='profile'),
    path('follow/', views.follow_user, name='follow'),
    path('unfollow/', views.unfollow_user, name='unfollow'),
    path('following/', views.following_list, name='following-list'),
    path('followers/', views.followers_list, name='followers-list'),
    path('user/<int:user_id>/', views.user_profile_detail, name='user-profile-detail'),
]