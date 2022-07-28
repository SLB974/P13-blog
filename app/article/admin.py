from django.contrib import admin

from .models import Article, ArticleCategory, Category

admin.site.register(Category)
admin.site.register(Article)
admin.site.register(ArticleCategory)
