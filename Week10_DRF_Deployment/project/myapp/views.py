from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer


class PostListAPIView(APIView):
    def get(self,request):
        posts = Post.objects.all().order_by("-created_at")
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = PostSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(request.errors, status=status.HTTP_400_BAD_REQUEST)
    
    