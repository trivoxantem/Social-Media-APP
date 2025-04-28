from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed_view, name='feeds'),
    path('add-comment/', views.add_comment_ajax, name='add_comment_ajax'),
    path('login', views.login_user, name='login'), 
    path('signup', views.signup_user, name="signup"),
    path('logout', views.logout_view, name="logout"),
    path('like/', views.like_post, name='like_post'),
    path('profile/<str:username>/follow/', views.toggle_follow, name='toggle_follow'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),  # Place this FIRST
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('search/', views.search, name='search'),
    path('groups/', views.group_list, name='group_list'),
    path('groups/create/', views.create_group, name='create_group'),
    path('groups/search/', views.group_search, name='group_search'),
    path('groups/<int:group_id>/', views.group_chat, name='group_chat'),
    path('groups/<int:group_id>/send/', views.send_message, name='send_message'),
    path('groups/<int:group_id>/join/', views.join_group, name='join_group'),
    path('groups/<int:group_id>/leave/', views.leave_group, name='leave_group'),
    path('groups/<int:group_id>/send/', views.send_message, name='send_message'),
]
