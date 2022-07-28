from article.models import Article, ArticleCategory, Category
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.simple_tag(name='categories')
def get_categories(value):
    category = Category.objects.get(category=value)
    return ' (' + str(ArticleCategory.objects.filter(category_id=category.id).count()) + ')'
