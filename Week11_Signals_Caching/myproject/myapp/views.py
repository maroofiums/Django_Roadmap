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
