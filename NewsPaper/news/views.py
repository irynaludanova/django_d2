from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from django.core.paginator import Paginator
from .models import  Author, Category, Post, PostCategory, Mail
from .filters import PostFilter
from .forms import PostForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = list(PostCategory.objects.filter(
            post=self.kwargs['pk']).values('category', 'category__category'))
        sub = list(Mail.objects.filter(subscribers=self.request.user.id).
                   values('category'))
        context['subscribed'] = [s['category'] for s in sub]
        context['author_name'] = Post.objects.filter(id=self.kwargs['pk']).\
            values('author__author_id__last_name')[0]['author__author_id__last_name']
        return context


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


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

@login_required
def subscribe(request, pk):
    if not Mail.objects.check(subscribers=get_user_model().
                                objects.get(id=request.user.id),
                                category=Category.objects.get(id=pk)):
        Mail.objects.create(subscribers=get_user_model().
                            objects.get(id=request.user.id),
                            category=Category.objects.get(id=pk))
    return redirect('/news')
