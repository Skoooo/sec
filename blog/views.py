from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts' : posts}) # requset를 받아 render 메서드 호출, blog/post_list.html 출력

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":                 #안비어어있다면
        form = PostForm(request.POST)            #폼에서 받은 데이터를 PoastForm으로
        if form.is_valid():                      #폼이 안비어있다면
            post = form.save(commit=False)       #넘겨진 데이터를 post에 바로 저장 x
            post.author = request.user           #작성자 저장
            post.published_date = timezone.now() #게시일 저장
            post.save()                          #포스트 저장
            return redirect('post_detail', pk=post.pk) # 작성후 post_detail로 이동, detail 뷰는 pk변수 필요
    else:
        form = PostForm()                        #비어있다면
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):                      #수정을 위해 pk 필요
    post = get_object_or_404(Post, pk=pk)        #수정하고자 하는 굴의 instance 가져옴
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)       
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
# 쿼리셋 공식문서 https://docs.djangoproject.com/en/2.0/ref/models/querysets/