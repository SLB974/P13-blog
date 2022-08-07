from unittest.mock import patch

from django.test import TestCase
from factory.core.html_factory import HtmlFactory, HtmlProcessor


class TestHtmlProcessor(TestCase):
   
    def test_html_processor_build_html_with_title(self):
        value = HtmlProcessor("title", ("title",1)).build_html()
        expected ="<h1 class='article_h1'>title</h1>\n"
        self.assertEqual(value, expected)
   
    def test_html_processor_build_html_with_paragraph(self):
        value = HtmlProcessor("paragraph", "title").build_html()
        expected ="<p class='article_p'>title</p>\n"
        self.assertEqual(value, expected)
   
    def test_html_processor_build_html_with_list(self):
        value = HtmlProcessor("list", ("title",'title')).build_html()
        expected ="<ul class='article_ul'><li class='article_li'>title</li>\n<li class='article_li'>title</li>\n</ul>"
        self.assertEqual(value, expected)

    def test_html_processor_build_html_with_link(self):
        value = HtmlProcessor("link", ("www.gmail.com",'title', 'True')).build_html()
        expected ="<a href='www.gmail.com' target='_blank'>title</a>\n"
        self.assertEqual(value, expected)

    def test_html_processor_build_html_with_image(self):
        value = HtmlProcessor("image", ('www.gmail.com','title')).build_html()
        expected ="<img src='www.gmail.com' alt='title'/>\n"
        self.assertEqual(value, expected)

    def test_html_processor_build_html_with_code(self):
        value = HtmlProcessor("code", ('import re')).build_html()
        expected ="<pre class='prettyprint lang-py'>import re</pre>\n"
        self.assertEqual(value, expected)

    def test_html_processor_build_html_with_gabarit_tag_extends(self):
        value = HtmlProcessor("gabarit_tag", 'extends').build_html()
        expected ="{% extends 'base.html' %}\n"
        self.assertEqual(value, expected)

    def test_html_processor_build_html_with_gabarit_tag_startblock(self):
        value = HtmlProcessor("gabarit_tag", 'startblock').build_html()
        expected ="{% block content %}\n"
        self.assertEqual(value, expected)

    def test_html_processor_build_html_with_gabarit_tag_endblock(self):
        value = HtmlProcessor("gabarit_tag", 'endblock').build_html()
        expected ="{% endblock %}\n"
        self.assertEqual(value, expected)

    def test_html_processor_build_html_with_gabarit_tag_static(self):
        value = HtmlProcessor("gabarit_tag", 'static').build_html()
        expected ="{% load static %}\n"
        self.assertEqual(value, expected)

    def test_html_processor_build_html_with_br(self):
        value = HtmlProcessor("br", '1').build_html()
        expected ="<br>\n"
        self.assertEqual(value, expected)

    def test_html_processor_build_html_with_unknown(self):
        value = HtmlProcessor("plouc","whatever").build_html()
        expected ="Elément inconnu"
        self.assertEqual(value, expected)
        
class TestHtmlFactory(TestCase):
    
    def test_not_registered_error(self):
        self.assertTrue(HtmlFactory().create_object("plouc"), Exception)
                
