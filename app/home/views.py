"""Module providing views to app home"""

import logging

from article.models import Article, Category
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import redirect, render
from django.views import generic

logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'home/index.html')

def category(request):
    
    queryset = Category.objects.all()
    context = {'result': queryset}
    return render(request,"home/category.html", context)

def article(request):
    return render(request,"home/article.html")

def tuto(request):
    return render(request,"home/tuto.html")

def oops(request):
    return render(request,"home/oops.html")

