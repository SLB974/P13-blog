from article.models import Article, ArticleCategory, Category
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.simple_tag(name='categories')
def get_categories(value):
    return Category.get_formated_category_count(value)
