from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from django.core.paginator import Paginator
from .models import Post, Category
from .filters import PostFilter
from .forms import PostForm

class NewsList(ListView):
    model = Post
    template_name = 'news_list.html'
    context_object_name = 'news_list'
    ordering = '-pub_date'
    paginate_by = 5


class NewsDetail(DetailView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'


class NewsFilter(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'search'
    ordering = ['-pub_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class NewsAdd(CreateView):
    model = Post
    template_name = 'add.html'
    form_class = PostForm
    success_url = '/news/'


class NewsEdit(UpdateView):
    model = Post
    template_name = 'edit.html'
    form_class = PostForm
    success_url = '/news/'


class NewsDelete(DeleteView):
    model = Post
    template_name = 'delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'