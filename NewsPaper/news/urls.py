from django.urls import path
from .views import NewsList, NewsDetail, NewsFilter, NewsAdd, NewsEdit, NewsDelete, \
subscribe

urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>/', NewsDetail.as_view(), name='news'),
    path('search/', NewsFilter.as_view(), name='search'),
    path('add/', NewsAdd.as_view(), name='add'),
    path('<int:pk>/edit/', NewsEdit.as_view(), name='edit'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='delete'),
    path('<int:pk>/subscribe/', subscribe, name='subscribe_category'),
 ]
