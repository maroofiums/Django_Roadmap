from rest_framework.viewsets import ModelViewSet
from .models import Post
from .serializers import PostSerializer
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

@method_decorator(cache_page(60*15), name='dispatch')
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    