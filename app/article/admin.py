from django.contrib import admin

from .models import (Article, ArticleCategory, ArticleDetails, Category,
                     HtmlType)

admin.site.register(Category)
admin.site.register(Article)
admin.site.register(ArticleCategory)
admin.site.register(ArticleDetails)
admin.site.register(HtmlType)
