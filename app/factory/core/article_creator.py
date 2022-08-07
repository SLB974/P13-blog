"""managing imported article creation database"""
from article.models import Article, ArticleCategory, Category


class ArticleCreator():
    def __init__(self, html_dict, html_file):
        self.html_dict = html_dict
        self.html_file = html_file
        self.article = None
        
    def get_tuto(self):
        return True if "tuto" in self.html_dict["category"] else False
    
    def get_oops(self):
        return True if "oops" in self.html_dict["category"] else False
        
    def check_article(self):
        """Check if article already exists"""
        return True if Article.exists(self.html_dict["title"]) else False
        
    def append_database(self):
        self.create_category()
        self.create_article()
        self.create_article_category()
        return self.article
        
    def create_category(self):
        """Create category if not exists"""
        category = Category()
        for element in self.html_dict["category"]:
            if element != "tuto" and element != "oops":
                category.add_item(element)                     
                                       
    def create_article(self):
        """Create article"""
        title=self.html_dict["title"]
        tuto=self.get_tuto()
        oops=self.get_oops()
        intro=self.html_dict["intro"]
        template=self.html_file
        article = Article()
        self.article =article.add_item(title, tuto, oops, intro, template)
        

    
    def create_article_category(self):
        for element in self.html_dict["category"]:
            if element != "tuto" and element != "oops":
                category = Category.objects.get(category__exact=element)
                article_category = ArticleCategory(article_id=self.article,
                                                    category_id=category)
                article_category.save()
        