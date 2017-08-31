from .models import Comment
from .models import Post
from django import forms
from photowall.widgets.naver_map_widget import NaverMapPointWidget


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'lnglat': NaverMapPointWidget(attrs={'width': 200, 'height': 200}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']
