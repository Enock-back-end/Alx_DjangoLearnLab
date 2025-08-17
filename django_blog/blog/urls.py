from django.urls import path
from .views import (
    register_view, login_view, logout_view, profile_view,
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
)
from . import views
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView
from .views import (
    search_posts, posts_by_tag
)

urlpatterns = [
    # Authentication
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),

    # Blog CRUD
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
        # Post CRUD URLs
    path('', views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    # Comment URLs
    path('post/<int:post_id>/comments/new/', views.add_comment, name='add-comment'),
    path('comment/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='edit-comment'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='delete-comment'),

    path('posts/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-update'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

    # Comment CRUD
path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

 # --- Advanced Features ---
    path('search/', search_posts, name='post-search'),              # Search URL
    path('tags/<str:tag_name>/', posts_by_tag, name='posts-by-tag') # Tag filtering URL
]
