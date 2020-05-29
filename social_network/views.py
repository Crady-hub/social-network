from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post
from .serializer import PostSerializer, PostCreateSerializer

class PostView(APIView):
    """ Выводит список постов """

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        post = PostCreateSerializer(data=request.data)
        if post.is_valid(raise_exception=True):
            saved = post.save()
        return Response({"success": f"Post '{saved}' created"}, status=201)
