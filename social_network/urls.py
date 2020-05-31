from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.PostListCreateView.as_view()),
    path('post/like/', views.LikeUnlikeCreateUpdateView.as_view()),
    path('post/like/statics', views.LikeUnlikeListView.as_view())
]