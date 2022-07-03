from article.models import Article
from django.db import models


class Catalog(models.Model):
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    target=models.CharField(max_length=255)
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name
