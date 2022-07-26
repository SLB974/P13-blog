from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=255)
    pic=models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.category
    
class Article(models.Model):
    title = models.CharField(max_length=255)
    tuto = models.BooleanField(default=False)
    oops=models.BooleanField(default=False)
    intro=models.CharField(max_length=1500, null=False, default='')
    template=models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ArticleCategory(models.Model):
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    category_id=models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.article_id) + ' / ' + str(self.category_id)

