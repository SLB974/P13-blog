from article.models import Article
from django import template

register = template.Library()

@register.simple_tag(name='categories')
def get_categories(value):
    return Article.get_related_category(value)

@register.simple_tag(name='pics')
def get_pic(value):
    return Article.get_related_pic(value)
