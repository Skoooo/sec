from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts' : posts}) # requset를 받아 render 메서드 호출, blog/post_list.html 출력

# 쿼리셋 공식문서 https://docs.djangoproject.com/en/2.0/ref/models/querysets/