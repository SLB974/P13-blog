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
    def __init__(self, title, level):
        self.title = title
        self.level = level
        self.type ="title"
        
    def get_type(self):
        return self.type

    def build_html(self):
        return "<h{} class='article_h{}'>{}</h{}>".format(self.level, self.level, self.title, self.level)
               
class ParagraphHtml(Ihtml):
    """Paragraph html class"""
    def __init__(self, text):
        self.text = text
        self.type ="paragraph"

    def get_type(self):
        return self.type
    
    def build_html(self):
        return "<p class='article_p'>{}</p>".format(self.text)

class ListHtml(Ihtml):
    """List html class"""
    def __init__(self, items):
        self.items = items
        self.type="list"
        
    def get_type(self):
        return self.type

    def build_html(self):
        return ("<ul class='article_ul'>{}</ul>").format("".join(["<li class='article_li'>{}</li>".format(item) 
                                                                  for item in self.items]))
    
class LinkHtml(Ihtml):
    """Link html class"""
    def __init__(self, text, url, blank=False):
        self.text = text
        self.url = url
        self.blank = blank
        self.type ="link"
        
    def get_type(self):
        return self.type

    def build_html(self):
        return "<a href='{}' target='{}'>{}</a>".format(self.url, "_blank" if self.blank else "", self.text)

class ImageHtml(Ihtml):
    """Image html class"""
    def __init__(self, url, alt):
        self.url = url
        self.alt = alt
        self.type ="image"
        
    def get_type(self):
        return self.type

    def build_html(self):
        return "<img src='{}' alt='{}'/>".format(self.url, self.alt)
    
class CodeHtml(Ihtml):
    """Code html class"""
    def __init__(self, text):
        self.text = text
        self.type ="code"
        
    def get_type(self):
        return self.type
    
    def build_html(self):
        return "<pre class='prettyprint lang-py'>{}</pre>".format(self.text)
   

class ExtendHtml(Ihtml):
    """Basic html class"""
    
    def __init__(self):
        self.type ="extend"
        
    def get_type(self):
        return self.type

    def build_html(self):
        return "{% extends 'base.html' %}"
    
class BeginBlock(Ihtml):
    """Block content start html class"""
    
    def __init__(self):
        self.type ="begin_block"
        
    def get_type(self):
        return self.type

    def build_html(self):
        return "{% block content %}"
    
class EndBlock(Ihtml):
    """Block content end html class"""

    def __init__(self):
        self.type ="end_block"
        
    def get_type(self):
        return self.type

    def build_html(self):
        return "{% endblock %}"
    
class LoadStatic(Ihtml):
    """Load static html class"""
    
    def __init__(self):
        self.type = "static"
        
    def get_type(self):
        return self.type

    def build_html(self):
        return "{% load static %}"

class HtmlFactory:
    """html factory class"""
    def __init__(self):
        self.registered =[TitleHtml, ParagraphHtml, ListHtml, LinkHtml, ImageHtml, CodeHtml, 
                          ExtendHtml, BeginBlock, EndBlock, LoadStatic]
    
    @staticmethod
    def get_html(tag, *args):
        """get html class"""
        
        for class_ in self.registered:
            if class_.get_type() == tag:
                return class_(*args)
        
        
        
