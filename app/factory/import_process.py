from datetime import datetime

from article.models import Article, ArticleCategory, Category

from .article_creator import ArticleCreator
from .html_factory import HtmlFactory
from .parser import Parser
from .template_creator import TemplateCreator


class ImportProcessor():
    def __init__(self, file):
        self.file = file
        self.html_dict = Parser(self.file).get_html_dict()
        self.html_file = "article-" + datetime.now().strftime("%y%m%d-%H%M%S") + ".html"
        self.article_creator = ArticleCreator(self.html_dict, self.html_file)
        self.template_creator = TemplateCreator(self.html_dict, self.html_file)
        self.error_message = None
        
    def check_file(self):
        """Checking if file is valid"""
        value = True
        
        if self.html_dict["title"] == None:
            self.error_message = "Le titre est manquant"
            value = False
            
        if self.html_dict["category"] == None:
            self.error_message = "Au moins une catégorie est manquante"
            value = False
            
        if self.html_dict["intro"] == None:
            self.error_message = "L'introduction est manquante"
            value = False
            
        return value
    
    def get_error_message(self):
        return self.error_message
        
    def get_file_name(self):
        return self.html_file
    
 
    def process(self):
        if self.check_file:
            self.article_creator.append_database()
            self.template_creator.save_html()
            return self.html_file
        return self.error_message
            
            
    
                
                       
                

