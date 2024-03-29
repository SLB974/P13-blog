from django import template
from django.template.defaultfilters import stringfilter

default_topbar=['/home/', '/article/category/', '/article/list/', '/article/tutorial/', '/article/oops/', 
                '/accounts/login/', '/user/account/signup', '/mail/send_mail/', '/accounts/signup']

error_topbar=['/404/', '/500/', '/403/', '/400/']

register = template.Library()

@register.simple_tag(takes_context=True)
def is_default(context):
    full_path = context['request'].get_full_path()
    return True if full_path in default_topbar else False

@register.simple_tag(takes_context=True)
def is_login(context):
    full_path = context['request'].get_full_path()
    return True if full_path.startswith('/accounts/') else False
    

@register.simple_tag(takes_context=True)
def is_upload(context):
    full_path = context['request'].get_full_path()
    return True if full_path == '/factory/upload/' else False

@register.simple_tag(takes_context=True)
def is_article(context):
    full_path = context['request'].get_full_path()
    return True if (full_path.startswith('/article/article/')) and (full_path != '/article/article/') else False

@register.simple_tag(takes_context=True)
def is_category(context):
    full_path = context['request'].get_full_path()
    return True if (full_path.startswith('/article/category/')) and (full_path != '/article/category/') else False

@register.simple_tag(takes_context=True)
def is_error(context):
    full_path = context['request'].get_full_path()
    return True if full_path in error_topbar else False
        
