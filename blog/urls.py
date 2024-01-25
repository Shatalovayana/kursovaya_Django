from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='blog-create'),
    path('', BlogListView.as_view(), name='blog-list'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='blog-view'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='blog-edit'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='blog-delete'),
]