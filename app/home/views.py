"""Module providing views to app home"""

import logging

from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import redirect, render

logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'home/index.html')
