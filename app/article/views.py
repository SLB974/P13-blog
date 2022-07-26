from django.shortcuts import render

from .models import Article

# Create your views here.

def render_article(request, pk):
    """ looking for article with pk and render it """
    record = Article.objects.get(pk=pk)
    article = 'article/' + record.html_file + '.html'
    return render(request, article)
