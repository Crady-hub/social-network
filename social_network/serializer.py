from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """ Список постов """
    author = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class PostCreateSerializer(serializers.ModelSerializer):
    """ Создание поста """

    class Meta:
        model = Post
        fields = ('title', 'text', 'author')