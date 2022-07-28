from django import template
from django.template.defaultfilters import stringfilter

default_topbar=['/home/', '/home/category/', '/home/article/', '/home/tutorial/', '/home/oops/', 
                '/accounts/login/', '/accounts/register/']

register = template.Library()

@register.simple_tag(takes_context=True)
def is_default(context):
    full_path = context['request'].get_full_path()
    return True if full_path in default_topbar else False

@register.simple_tag(takes_context=True)
def is_upload(context):
    full_path = context['request'].get_full_path()
    return True if full_path == '/factory/upload/' else False

@register.simple_tag(takes_context=True)
def is_article(context):
    full_path = context['request'].get_full_path()
    if (full_path.startswith('/home/article/')) and (full_path != '/home/article/'):
        return True
    if (full_path.startswith('/home/tutorial/')) and (full_path != '/home/tutorial/'):
        return True
    if (full_path.startswith('/home/oops/')) and (full_path != '/home/oops/'):
        return True
    return False

@register.simple_tag(takes_context=True)
def is_category(context):
    full_path = context['request'].get_full_path()
    if (full_path.startswith('/home/category/')) and (full_path != '/home/category/'):
        return True
    return False
        
