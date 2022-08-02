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
        return False
    
    @staticmethod
    def get_count():
        return Category.objects.count()
    
    @staticmethod  
    def get_formated_count():
        count = Category.objects.count()
        return f"({count})"

    @staticmethod
    def get_formated_category_count(category):
        return f"({ArticleCategory.objects.filter(category_id__category__exact=category).count()})"
       
    @staticmethod 
    def get_list():
        return Category.objects.all().order_by('category')
    
    @staticmethod
    def get_item(category):
        return Category.objects.get(category__exact=category)
        
    @staticmethod
    def get_related_articles(category):
        return Category.get_item(category).categories.all()

    
    def add_item(self, item):
        if not self.exists(item):
            category = Category(category=item)
            category.save()
            return category
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
    def get_count():
        return Article.objects.count()
    
    @staticmethod
    def get_formated_count():
        count = Article.objects.count()
        return f"({count})"
    
    @staticmethod
    def get_tuto_count():
        return f"({Article.objects.filter(tuto=True).count()})"
    
    @staticmethod
    def get_oops_count():
        return f"({Article.objects.filter(oops=True).count()})"
    
    @staticmethod
    def exists(item):
        if Article.objects.filter(title__exact=item):
            return True
        return False
        
    @staticmethod
    def get_list():
        return Article.objects.all().order_by('-created_at')
  
    @staticmethod
    def get_tuto_list():
        return Article.objects.filter(tuto=True).order_by('-created_at')
    
    @staticmethod
    def get_oops_list():
        return Article.objects.filter(oops=True).order_by('-created_at')
    
    @staticmethod
    def get_list_category(category):
        return Article.objects.filter(articles__category_id__category__exact=category).order_by('-created_at')     
    
    @staticmethod
    def get_item(title):
        return Article.objects.get(title__exact=title)
          
    @staticmethod
    def get_related_category(title):
        return Article.get_item(title).articles.all().values_list('category_id__category', flat=True)
    
    @staticmethod
    def get_related_pic(title):
        return 'assets/img/' + Article.get_item(title).articles.all(
            ).values_list('category_id__pic', flat=True).first()
    
    @staticmethod
    def get_all_related_categories():
        return ArticleCategory.objects.all().values_list('category_id__category', flat=True).distinct().order_by(
            'category_id__category')
           
    @staticmethod
    def get_all_related_pics():
        return ArticleCategory.objects.all().values_list('category_id__pic', flat=True).distinct().order_by(
            'category_id__pic')
    
    def add_item(self, title, tuto, oops, intro, template):
        if not self.exists(title):
            article = Article(title=title, tuto=tuto, oops=oops, intro=intro, template=template)
            article.save()
            return article
        else:
            return Article.objects.get(title__exact=title)
        
    @staticmethod
    def get_template(title):
        article =  Article.objects.get(title__exact=title)
        return article.template
        
class ArticleCategory(models.Model):
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='articles', 
                                   related_query_name='articles')
    category_id=models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categories",
                                  related_query_name="categories")
    def __str__(self):
        return str(self.article_id) + ' / ' + str(self.category_id)
  
    @staticmethod
    def add_item(article_id, category_id):
        article_category = ArticleCategory(article_id=article_id, category_id=category_id)
        article_category.save()
        return article_category

