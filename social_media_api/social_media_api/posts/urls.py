from django.urls import path
from . import views

urlpatterns = [
    # Example route just to avoid errors for now
    path("", views.index, name="posts-home"),
]