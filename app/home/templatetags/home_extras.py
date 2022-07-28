from article.models import Article, Category
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.simple_tag(name='details')
def get_details(value):
    
    if value=="category":
        return '('+ str(Category.objects.count()) + ')'

    elif value=="article":
        return '('+ str(Article.objects.count()) + ')'
    
    elif value=="tuto":
        return '('+str(Article.objects.filter(tuto=True).count())+')'
    
    elif value=='oops':
        return '('+str(Article.objects.filter(oops=True).count())+')'
    
    else:
        return ''
