"""Providing views to app article"""
import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .models import Article, ArticleCategory, Category

logger = logging.getLogger(__name__)

def category_list(request):
    context = {'result': Category.get_list()}
    return render(request,"article/category_list.html", context)

def essai(request, category):
    context = {"result": Article.get_list_category(category),
               "category":category,}
    return render(request,"article/essai.html", context)

def category(request, category):
    context = {"result": Article.get_list_category(category),
               "category":category,}
    return render(request,"article/category.html", context)

def article_list(request):
    context = {"result": Article.get_list(),
               "categories":Article.get_all_related_categories(),
               "pics":Article.get_all_related_pics(),}

    return render(request,"article/article_list.html", context)

def tuto_list(request):
    context = {"result": Article.get_tuto_list(), 
               "categories":Article.get_all_related_categories(),
               "pics":Article.get_all_related_pics(),}
    return render(request,"article/tuto_list.html", context)

def oops_list(request):
    context = {"result": Article.get_oops_list(), 
               "categories":Article.get_all_related_categories(),
               "pics":Article.get_all_related_pics(),}
    return render(request,"article/oops_list.html", context)

def article(request, title):
    context = {"title":title,
               "categories":Article.get_related_category(title),
               "pics":Article.get_related_pic(title),}
    template = Article.get_template(title)
    return render(request,template, context)


