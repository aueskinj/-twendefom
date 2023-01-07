from django.urls import path
from .views import PostListView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    #int:pk-> inputing as a variable pk, int var from view.py
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
]
