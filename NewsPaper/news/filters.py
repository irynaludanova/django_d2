from django_filters import FilterSet
from .models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'pub_date': ['gt'],
            'header': ['icontains'],
            'author.author_id.last_name': ['icontains'],
        }
