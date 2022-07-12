from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=255)
    pic=models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.category
    
class HtmlType(models.Model):
    html_type = models.CharField(max_length=255)

    def __str__(self):
        return self.html_type

class Article(models.Model):
    title = models.CharField(max_length=255)
    tuto = models.BooleanField(default=False)
    oops=models.BooleanField(default=False)
    intro=models.CharField(max_length=1500, null=False, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    url=models.URLField(max_length=255, null=True)

    def __str__(self):
        return self.title

class ArticleCategory(models.Model):
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    category_id=models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.article_id) + ' / ' + str(self.category_id)

class ArticleDetails(models.Model):
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    details = models.CharField(max_length=1500, null=False)
    type= models.ForeignKey(HtmlType, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.article_id) + ' / ' + self.details
