from django.forms import ModelForm, BooleanField
from .models import Post


class PostForm(ModelForm):
    check_box = BooleanField(label='Check!')

    class Meta:
        model = Post
        fields = ['author', 'type', 'categories', 'header', 'text']