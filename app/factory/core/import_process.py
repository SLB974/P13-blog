from datetime import datetime

from django.core.files.storage import FileSystemStorage

from .article_creator import ArticleCreator
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
    
    def get_html_dict(self):
        return self.html_dict
    
    def check_file(self):
        """Checking if file is valid"""
        
        if not "title" in self.get_html_dict():
            self.error_message = "Le fichier doit contenir un titre."
            return False
            
        if not "category" in self.get_html_dict():
            self.error_message = "Le fichier doit contenir au moins une catégorie."
            return False
            
        if not "intro" in self.get_html_dict():
            self.error_message = "Le fichier doit contenir une introduction."
            return False
        
        if self.article_creator.check_article():
            self.error_message = "Cet article a déjà été importé."
            return False
            
        return True
    
    def get_error_message(self):
        return self.error_message
        
    def get_file_name(self):
        return self.html_file
    
    def kill_file(self):
        fs = FileSystemStorage()
        fs.delete(self.file)
    
    def process(self):
        if self.check_file():
            self.article_creator.append_database()
            self.template_creator.save_html()
            self.kill_file()
            return self.html_dict['title']
        
        self.kill_file()
        raise Exception(self.get_error_message())            
            
    
                
                       
                

