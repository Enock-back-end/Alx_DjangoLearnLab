from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView, index
from django.urls import path, include
from .views import PostViewSet, CommentViewSet, FeedView, index, LikePostView, UnlikePostView
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView, LikePostView, UnlikePostView


router = DefaultRouter()
router.register(r"posts", PostViewSet, basename="post")
router.register(r"comments", CommentViewSet, basename="comment")

urlpatterns = [
    path("", index, name="posts-home"),
    path("", include(router.urls)),
    path("feed/", FeedView.as_view(), name="feed"),
    path("", index, name="posts-home"),
    path("", include(router.urls)),
    path("feed/", FeedView.as_view(), name="feed"),
    path("posts/<int:pk>/like/", LikePostView.as_view(), name="like-post"),
    path("posts/<int:pk>/unlike/", UnlikePostView.as_view(), name="unlike-post"),
]



