from rest_framework import permissions
from rest_framework import generics

from .models import Post
from .serializer import PostListSerializer, PostCreateSerializer


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostListSerializer
        elif self.request.method == 'POST':
            return PostCreateSerializer

#class PostView(APIView):
#     """ Выводит список постов """

#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         post = PostCreateSerializer(data=request.data)
#         if post.is_valid(raise_exception=True):
#             saved = post.save()
#         return Response({"success": f"Post '{saved}' created"}, status=201)
