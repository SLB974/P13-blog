"""Module providing views to app home"""

import logging

from article.models import Article, ArticleCategory, Category
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import redirect, render
from django.views import generic

logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'home/index.html')

def category_list(request):
    context = {'result': Category.get_list()}
    return render(request,"home/category_list.html", context)

def category(request, category):
    object = Category()
    context = {"result": object.get_related(category),
               "category":category}
    return render(request,"home/category.html", context)

def article_list(request):
    context = {"result": Article.get_list()}
    return render(request,"home/article_list.html", context)

def article(request, title):
    object = Article()
    related = object.get_related(title)
    template = object.get_item(title).template
    context = {"result":{"title": title,
               "categories": related,}}
    return render(request,template, context)

def tuto_list(request):
    context = {"result": Article.get_tuto_list(), "template_name": "home/tuto_list.html"}
    return render(request,"home/tuto_list.html", context)

def tuto(request, title):
    object = Article()
    related = object.get_related(title)
    template = object.get_item(title).template
    context = {"result":{"title": title,
               "categories": related,}}
    return render(request,template, context)

def oops_list(request):
    context = {"result": Article.get_oops_list()}
    return render(request,"home/oops_list.html", context)

def oops(request, title):
    object = Article()
    related = object.get_related(title)
    template = object.get_item(title).template
    context = {"result":{"title": title,
               "categories": related,}}
    return render(request,template, context)

