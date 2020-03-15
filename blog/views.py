from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {}) # requset를 받아 render 메서드 호출, blog/post_list.html 출력
