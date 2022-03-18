from django.urls import path
from django.contrib import admin

from .views import HomeView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [
    path("posts/", HomeView.as_view(), name="blog-home"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/create", PostCreateView.as_view(), name="post-create"),
    path("posts/update/<int:pk>", PostUpdateView.as_view(), name="post-update"),
    path("posts/delete/<int:pk>", PostDeleteView.as_view(), name="post-delete")
]
