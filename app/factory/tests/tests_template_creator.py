from unittest.mock import patch

from django.test import TestCase
from factory.core.template_creator import TemplateCreator


class TestTemplateCreator(TestCase):
    
    def setUp(self):
        self.html_dict = {
            "title": "This is a title",
            "category": ["Python", "Docker"],
            "intro": "This is an intro",
            "content": [("paragraph", "This is a paragraph")]       
            }
        self.html_file="test.html"
        self.creator = TemplateCreator(self.html_dict, self.html_file)
        
    def test_get_file_full_path(self):
        actual = self.creator.get_file_full_path()
        expected = "mediafiles/generated_templates/test.html"
        self.assertTrue(actual == expected)
    
    @patch('factory.tests.tests_template_creator.TemplateCreator.start_html')
    @patch('factory.tests.tests_template_creator.TemplateCreator.introduction_html')
    @patch('factory.tests.tests_template_creator.TemplateCreator.content_html')
    @patch('factory.tests.tests_template_creator.TemplateCreator.end_html')
    def test_build_html_calls_proper_methods(self, end_html, content_html, introduction_html, start_html):
        self.creator.build_html()
        self.assertTrue(start_html.called)
        self.assertTrue(introduction_html.called)
        self.assertTrue(content_html.called)
        self.assertTrue(end_html.called)
        
    
    @patch('factory.core.template_creator.HtmlProcessor')
    def test_start_html_calls_html_processor(self, mockClass):
        self.creator.start_html()
        expected = 3
        self.assertTrue( mockClass.call_count == expected)
  
    @patch('factory.core.template_creator.HtmlProcessor')
    def test_end_html_calls_html_processor(self, mockClass):
        self.creator.end_html()
        self.assertTrue( mockClass.called)
  
    @patch('factory.core.template_creator.HtmlProcessor')
    def test_introduction_calls_html_processor(self, mockClass):
        self.creator.introduction_html()
        self.assertTrue( mockClass.called)
  
    @patch('factory.core.template_creator.HtmlProcessor')
    def test_content_html_calls_html_processor_n_content_times(self, mockClass):
        self.creator.content_html()
        expected = self.html_dict["content"].__len__()
        self.assertTrue( mockClass.call_count, expected)
        