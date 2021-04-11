from django.views.generic import ListView, DetailView
from .models import Post

class NewsList(ListView):
    model = Post
    template_name = 'news_list.html'
    context_object_name = 'news'
    ordering = '-pub_date'
    paginate_by = 10


class NewsDetail(DetailView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'new'
