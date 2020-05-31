from rest_framework import serializers

from .models import Post, LikeUnlike


class PostListSerializer(serializers.ModelSerializer):
    """ Список постов """

    author = serializers.SlugRelatedField(
        slug_field="username", read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class PostCreateSerializer(serializers.ModelSerializer):
    """ Создание поста """

    class Meta:
        model = Post
        exclude = ('pub_date',)


class LikeUnlikeCreateUpdateSerializer(serializers.ModelSerializer):
    """ Создание/обновление лайков """

    class Meta:
        model = LikeUnlike
        fields = '__all__'

    def create(self, validate_data):
        like_unlike, _ = LikeUnlike.objects.update_or_create(
            post=validate_data.get('post', None),
            user=validate_data.get('user', None),
            defaults={'like': validate_data.get('like')}
        )
        return like_unlike


class LikeUnlikeListSerializer(serializers.ModelSerializer):
    """ Вывод количества лайков в диапазоне дат """

    likes = serializers.IntegerField()

    class Meta:
        model = LikeUnlike
        fields = ('date', 'likes',)
