"""Implementing factory design pattern for building HTML content"""

from abc import ABCMeta, abstractmethod


class Ihtml(metaclass=ABCMeta):
    """html interface"""
    
    @staticmethod
    @abstractmethod
    def build_html():
        """Abstract method for building HTML content"""

class TitleHtml(Ihtml):
    """Title html class"""
    def __init__(self, title, level):
        self.title = title
        self.level = level

    def build_html(self):
        
        if self.level==1:
            return "<h1>" + self.title + "</h1>"
        
        elif self.level==2:
            return "<h2>" + self.title + "</h2>"
        
        elif self.level==3:
            return "<h3>" + self.title + "</h3>"

class ParagraphHtml(Ihtml):
    """Paragraph html class"""
    def __init__(self, text):
        self.text = text

    def build_html(self):
        return "<p class='ip'>" + self.text + "</p>"

class ListHtml(Ihtml):
    """List html class"""
    def __init__(self, items):
        self.items = items

    def build_html(self):
        return "<ul class='iul'>" + "".join(["<li>" + item + "</li>" for item in self.items]) + "</ul>"
    
class LinkHtml(Ihtml):
    """Link html class"""
    def __init__(self, text, url, blank=False):
        self.text = text
        self.url = url
        self.blank = blank

    def build_html(self):
        return "<a class='ilink' href=\"" + self.url + "\">" + self.text + "</a>"

class ImageHtml(Ihtml):
    """Image html class"""
    def __init__(self, url, alt):
        self.url = url
        self.alt = alt

    def build_html(self):
        return "<img class='iimage' src=\"" + self.url + "\" alt=\"" + self.alt + "\">"
    
class CodeHtml(Ihtml):
    """Code html class"""
    def __init__(self, text, language):
        self.text = text
        self.language = language

    def build_html(self):
        return "<pre class='icode'><code class='" + self.language + "'>" + self.text + "</code></pre>"
    
class HtmlFactory:
    """html factory class"""
    
    @staticmethod
    def get_html(tag, *args):
        """get html class"""
        if tag == "title":
            return TitleHtml(*args)
        elif tag == "paragraph":
            return ParagraphHtml(*args)
        elif tag == "list":
            return ListHtml(*args)
        elif tag == "link":
            return LinkHtml(*args)
        elif tag == "image":
            return ImageHtml(*args)
        elif tag == "code":
            return CodeHtml(*args)
        else:
            return None
