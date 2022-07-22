"""managing imported article creation database"""
from article.models import Article, ArticleCategory, Category


class ArticleCreator():
    def __init__(self, html_dict, html_file):
        self.html_dict = html_dict
        self.html_file = html_file
        self.article = None
        
    def get_tuto(self):
        if "tuto" in self.html_dict["category"]:
            return True
        else:
            return False
    
    def get_oops(self):
        if "oops" in self.html_dict["category"]:
            return True
        else:
            return False
        
    def append_database(self):
        self.create_category()
        self.create_article()
        self.create_article_category()
        
    def create_category(self):
        """Create category if not exist"""
        
        for element in self.html_dict["category"]:
            if element != "tuto" and element != "oops":
                if Category.objects.get(category=element) == None:
                    category = Category(category=element)
                    category.save()                       
                                       
    def create_article(self):
        """Create article"""
        article = Article(title=self.html_dict["title"],
                          tuto=self.get_tuto(),
                          oops=self.get_oops(),
                          intro=self.html_dict["intro"],
                          template=self.html_file)
        article.save()
        self.article = article
    
    def create_article_category(self):
        for element in self.html_dict["category"]:
            if element != "tuto" and element != "oops":
                category = Category.objects.get(category=element)
                article_category = ArticleCategory(article_id=self.article,
                                                    category_id=category)
                article_category.save()
        