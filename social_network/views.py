from rest_framework import generics, permissions
from django_filters import rest_framework as filters
from django.db.models import Count, Q

from .models import Post, LikeUnlike
from .serializer import (
    PostListSerializer,
    PostCreateSerializer,
    LikeUnlikeCreateUpdateSerializer,
    LikeUnlikeListSerializer
)


class PostListCreateView(generics.ListCreateAPIView):
    """ Выводит/создает пост """

    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostListSerializer
        elif self.request.method == 'POST':
            return PostCreateSerializer


class LikeUnlikeFilter(filters.FilterSet):
    """ Фильтр для выбора диапазона дат"""
    date = filters.DateFromToRangeFilter()

    class Meta:
        model = LikeUnlike
        fields = ('date',)


class LikeUnlikeCreateUpdateView(generics.CreateAPIView):
    """ Создаем/обновляем/список лайк """

    queryset = LikeUnlike.objects.all()
    serializer_class = LikeUnlikeCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]


class LikeUnlikeListView(generics.ListAPIView):
    """ Список дат с количеством лайков """

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = LikeUnlikeFilter
    serializer_class = LikeUnlikeListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        likes = LikeUnlike.objects.values('date').annotate(
            likes=Count('like', filter=Q(like=True)))
        return likes
