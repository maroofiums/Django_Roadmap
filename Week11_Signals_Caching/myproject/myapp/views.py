from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.views import View
from django.shortcuts import render
from .models import Post

@method_decorator(cache_page(60 * 5), name='dispatch')  # 5 minutes cache
class HomeView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'home.html', {'recent_posts': posts})
from django.core.cache import cache

def get_popular_posts(request):
    posts = cache.get('popular_posts')

    if not posts:
        posts = Post.objects.order_by('-created_at')[:5]
        cache.set('popular_posts', posts, timeout=30)

    return render(request, "popular.html", {"posts": posts})
