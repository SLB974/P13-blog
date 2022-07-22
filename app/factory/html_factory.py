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
    def __init__(self, content):
        self.title = content[0]
        self.level = content[1]
        self.name ="title"
        
    def get_type(self):
        return self.name

    def build_html(self):
        return "<h{} class='article_h{}'>{}</h{}>\n".format(self.level, self.level, self.title, self.level)
               
class ParagraphHtml(Ihtml):
    """Paragraph html class"""
    def __init__(self, text):
        self.text = text
        self.name ="paragraph"

    def get_type(self):
        return self.name
    
    def build_html(self):
        return "<p class='article_p'>{}</p>\n".format(self.text)

class ListHtml(Ihtml):
    """List html class"""
    def __init__(self, items):
        self.items = items
        self.name="list"
        
    def get_type(self):
        return self.name

    def build_html(self):
        return ("<ul class='article_ul'>{}</ul>").format("".join(["<li class='article_li'>{}</li>\n".format(item) 
                                                                  for item in self.items]))
    
class LinkHtml(Ihtml):
    """Link html class"""
    def __init__(self, values):
        self.url = values[0]
        self.text = values[1]
        self.blank = lambda x: True if values[2] == "True" else False
        self.name ="link"
        
    def get_type(self):
        return self.name

    def build_html(self):
        return "<a href='{}' target='{}'>{}</a>\n".format(self.url, "_blank" if self.blank else "", self.text)

class ImageHtml(Ihtml):
    """Image html class"""
    def __init__(self, url, alt):
        self.url = url
        self.alt = alt
        self.name ="image"
        
    def get_type(self):
        return self.name

    def build_html(self):
        return "<img src='{}' alt='{}'/>\n".format(self.url, self.alt)
    
class CodeHtml(Ihtml):
    """Code html class"""
    def __init__(self, code):
        self.code = code
        self.name ="code"
        
    def get_type(self):
        return self.name
    
    def build_html(self):
        return "<pre class='prettyprint lang-py'>{}</pre>\n".format(self.code)
   

class ExtendHtml(Ihtml):
    """Basic html class"""

    def __init__(self):
        self.name ="extend"
        
    def get_type(self):
        return self.name

    def build_html(self):
        return "{% extends 'base.html' %}\n"
    
class BeginBlock(Ihtml):
    """Block content start html class"""
    
    def __init__(self):
        self.name ="start_block"
        
    def get_type(self):
        return self.name

    def build_html(self):
        return "{% block content %}\n"
    
class EndBlock(Ihtml):
    """Block content end html class"""

    def __init__(self):
        self.name ="end_block"
        
    def get_type(self):
        return self.name

    def build_html(self):
        return "{% endblock %}\n"
    
class LoadStatic(Ihtml):
    """Load static html class"""
    
    def __init__(self):
        self.name = "static"
        
    def get_type(self):
        return self.name

    def build_html(self):
        return "{% load static %}\n"
    
class BrHtml(Ihtml):
    """Load static html class"""
    
    def __init__(self):
        self.name = "br"
        
    def get_type(self):
        return self.name

    def build_html(self):
        return "<br>\n"


class HtmlFactory:
    """html factory class"""
    
    registered =[TitleHtml, ParagraphHtml, ListHtml, LinkHtml, ImageHtml, CodeHtml, 
                          ExtendHtml, BeginBlock, EndBlock, LoadStatic]
    
    @staticmethod
    def get_html_class(tag, *args):
        """get html class"""
    
        if tag == "title":
            return TitleHtml(args[0])
        
        if tag == "paragraph":
            return ParagraphHtml(args[0])
        
        if tag == "list":
            return ListHtml(args[0])
        
        if tag == "link":
            return LinkHtml(args[0])
        
        if tag == "image":
            return ImageHtml(args[0], args[1])
        
        if tag=="code":
            return CodeHtml(args[0])
        
        if tag=="extend":
            return ExtendHtml()
        
        if tag=="start_block":
            return BeginBlock()
        
        if tag=="end_block":
            return EndBlock()
        
        if tag=="static":
            return LoadStatic()
        
        if tag =='br':
            return BrHtml()
        
        
        
