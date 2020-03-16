from django import forms

from .models import Post

class PostForm(forms.ModelForm): # forms.ModelFrom : 장고에 모델폼이라고 알려줌

    class Meta:
        model = Post
        fields = ('title', 'text',)