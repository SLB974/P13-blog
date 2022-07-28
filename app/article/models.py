from os import stat

from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=255)
    pic=models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.category
    
    @staticmethod
    def exists(item):
        if Category.objects.filter(category__exact=item):
            return True
        else:
            return False
       
    @staticmethod 
    def get_list():
        return Category.objects.all().order_by('category')
    
    @staticmethod
    def get_item(category):
        return Category.objects.get(category__exact=category)
        
    def get_related(self, category):
        queryset = ArticleCategory.objects.filter(category_id__exact = self.get_item(category)).values_list('article_id', flat=True)
        return Article.objects.filter(id__in=queryset)
    
    def add_item(self, item):
        if not self.exists(item):
            category = Category(category=item)
            category.save()
            return category
        else:
            return Category.objects.get(category__exact=item)
        
class Article(models.Model):
    title = models.CharField(max_length=255)
    tuto = models.BooleanField(default=False)
    oops=models.BooleanField(default=False)
    intro=models.CharField(max_length=1500, null=False, default='')
    template=models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    @staticmethod
    def exists(item):
        if Article.objects.filter(title__exact=item):
            return True
        else:
            return False
        
    @staticmethod
    def get_list():
        return Article.objects.all()
    
    @staticmethod
    def get_tuto_list():
        return Article.objects.filter(tuto=True)
    
    @staticmethod
    def get_oops_list():
        return Article.objects.filter(oops=True)
    
    @staticmethod
    def get_item(title):
        return Article.objects.get(title__exact=title)
          
    def get_related(self, title):
        return ArticleCategory.objects.filter(article_id__exact=self.get_item(title)).values('category_id')

    def add_item(self, title, tuto, oops, intro, template):
        if not self.exists(title):
            article = Article(title=title, tuto=tuto, oops=oops, intro=intro, template=template)
            article.save()
            return article
        else:
            return Article.objects.get(title__exact=title)
        
        
class ArticleCategory(models.Model):
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    category_id=models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.article_id) + ' / ' + str(self.category_id)
    
    @staticmethod
    def add_item(article_id, category_id):
        article_category = ArticleCategory(article_id=article_id, category_id=category_id)
        article_category.save()
        return article_category

