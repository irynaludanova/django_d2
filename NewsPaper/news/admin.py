from django.contrib import admin
from .models import Mail, Post, Comment, Author, Category, PostCategory

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(PostCategory)
admin.site.register(Mail)
