from article.models import Article, Category
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.simple_tag(name='details')
def get_details(value):
    
    if value=="category":
        return Category.get_formated_count()

    elif value=="article":
        return Article.get_formated_count()
    
    elif value=="tuto":
        return Article.get_tuto_count()
    
    elif value=='oops':
        return Article.get_oops_count()
    
    else:
        return ''
