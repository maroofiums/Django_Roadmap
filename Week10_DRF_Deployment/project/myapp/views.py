from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer


# class PostListAPIView(APIView):
#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)


# class PostDetailAPIView(APIView):
#     def get(self,request,pk):
#         try:
#             post = Post.objects.get(pk=pk)
#         except Post.DoesNotExist:
#             return Response({"error":"Post Not Found"},status=status.HTTP_404_NOT_FOUND)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)

# class PostCreateAPI(APIView):
#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

# class PostUpdateAPI(APIView):
#     def put(self, request, pk):
#         post = Post.objects.get(pk=pk)
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)

# class PostDeleteAPI(APIView):
#     def delete(self, request, pk):
#         post = Post.objects.get(pk=pk)
#         post.delete()
#         return Response({"message": "deleted"})

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer

