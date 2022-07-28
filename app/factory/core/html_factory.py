"""Implementing factory design pattern for building HTML content"""

from abc import ABCMeta, abstractmethod


class Ihtml(metaclass=ABCMeta):
    """html interface"""
    
    @staticmethod
    @abstractmethod
    def build_html():
        """Abstract method for building HTML content"""
        
    @staticmethod
    @abstractmethod
    def get_type():
        """Abstract method for getting type html type"""

class TitleHtml(Ihtml):
    """Title html class"""
    
    type ="title"
    
    def __init__(self, content):
        self.title = content[0]
        self.level = content[1]
     
    @classmethod    
    def get_type(cls):
        return cls.type

    def build_html(self):
        return "<h{} class='article_h{}'>{}</h{}>\n".format(self.level, self.level, self.title, self.level)
               
class ParagraphHtml(Ihtml):
    """Paragraph html class"""
        
    type ="paragraph"
    
    def __init__(self, content):
        self.content = content

    @classmethod
    def get_type(cls):
        return cls.type
    
    def build_html(self):
        return "<p class='article_p'>{}</p>\n".format(self.content)

class ListHtml(Ihtml):
    """List html class"""

    type="list"

    def __init__(self, content):
        self.content = content
    
    @classmethod    
    def get_type(cls):
        return cls.type

    def build_html(self):
        return ("<ul class='article_ul'>{}</ul>").format("".join(["<li class='article_li'>{}</li>\n".format(item) 
                                                                  for item in self.content]))
    
class LinkHtml(Ihtml):
    """Link html class"""
    
    type ="link"
    
    def __init__(self, content):
        self.url = content[0]
        self.text = content[1]
        self.blank = lambda x: True if content[2] == "True" else False
    
    @classmethod   
    def get_type(cls):
        return cls.type

    def build_html(self):
        return "<a href='{}' target='{}'>{}</a>\n".format(self.url, "_blank" if self.blank else "", self.text)

class ImageHtml(Ihtml):
    """Image html class"""
    
    type ="image"
    
    def __init__(self, content):
        self.url = content[0]
        self.alt = content[1]

    @classmethod        
    def get_type(cls):
        return cls.type

    def build_html(self):
        return "<img src='{}' alt='{}'/>\n".format(self.url, self.alt)
    
class CodeHtml(Ihtml):
    """Code html class"""
    
    type = "code"
    
    def __init__(self, content):
        self.code = content
        
    @classmethod        
    def get_type(cls):
        return cls.type
    
    def build_html(self):
        return "<pre class='prettyprint lang-py'>{}</pre>\n".format(self.code)
   
class GabaritTagHtml(Ihtml):
    """Gabarit Tag html class"""
    
    type = "gabarit_tag"
    
    
    def __init__(self, content):
        self.content = content
        
    @classmethod        
    def get_type(cls):
        return cls.type

    def build_html(self):
        
        if self.content == "extends":
            return "{% extends 'base.html' %}\n"
        
        elif self.content =="startblock":
            return "{% block content %}\n"
        
        elif self.content =="endblock":
            return "{% endblock %}\n"
        
        elif self.content =="static":
            return "{% load static %}\n"

class BrHtml(Ihtml):
    """br html class"""
    
    type = "br"
    
    def __init__(self, content):
        self.content = int(content)
        
    @classmethod        
    def get_type(cls):
        return cls.type

    def build_html(self):
        br = ""
        if self.content != 0:
            for _ in range(self.content):
                br +=  "<br>\n"
        return br


class HtmlFactory:
    """html factory class"""
    
    @staticmethod
    def create_object(type):
        """return proper class based on type"""
        registered =[TitleHtml, ParagraphHtml, ListHtml, LinkHtml, ImageHtml, CodeHtml, 
                            GabaritTagHtml, BrHtml]
        
        for class_ in registered:
            
            try:
                if class_.get_type() == type:
                    return class_
                
            except:
                return Exception("Unknown type")   
        
        
        
class HtmlProcessor:
    def __init__(self, type, content):
        self.type = type
        self.content = content
        self.html_object = HtmlFactory.create_object(type)       
        
    def build_html(self):
        try:
            return self.html_object(self.content).build_html()
        except:
            return "Elément inconnu"
