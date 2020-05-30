from rest_framework import permissions
from rest_framework import generics
from django_filters import rest_framework as filters

from .models import Post, LikeUnlike
from .serializer import (
    PostListSerializer,
    PostCreateSerializer,
    LikeUnlikeCreateUpdateSerializer
)


class PostListCreateView(generics.ListCreateAPIView):
    """ Выводит/создает пост """

    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostListSerializer
        elif self.request.method == 'POST':
            return PostCreateSerializer


class LikeUnlikeFilter(filters.FilterSet):
    date = filters.DateFromToRangeFilter()

    class Meta:
        model = LikeUnlike
        fields = ('date',)

class LikeUnlikeCreateUpdateView(generics.ListCreateAPIView):
    """ Создаем/обновляем/список лайк """

    queryset = LikeUnlike.objects.all()
    serializer_class = LikeUnlikeCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = LikeUnlikeFilter

