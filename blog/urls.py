from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), # ''문자열일때 post_list를 보여줌
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]

# url 설정 https://docs.djangoproject.com/en/2.0/topics/http/urls/