import types
from unittest.mock import patch

from django.test import TestCase
from factory.core.parser import Parser


class TestParser(TestCase):
    
    def setUp(self):
        self.file = "factory/tests/test_file.md"
        self.parser = Parser(self.file)


    def test_generator_list_returns_generator(self):
        self.assertIsInstance(self.parser.generator_list(), 
                              types.GeneratorType)
        
    def test_generator_list_returns_18_lines(self):
        self.assertEqual(len(list(self.parser.generator_list())), 18)
    
    def test_append_html_dict_content_adds_content_to_dict(self):
        before = len(self.parser.html_dict['content'])
        self.parser.append_html_dict_content('paragraph', 'This is a paragraph')
        after = len(self.parser.html_dict['content'])
        self.assertEqual(before + 1, after)
        
    def test_update_html_dict_adds_content_to_dict(self):
        self.parser.update_html_dict('title', 'This is a title')
        actual = self.parser.html_dict['title']
        expected = 'This is a title'
        self.assertEqual(actual, expected)
        
    def test_get_html_dict_calls_parse(self):
        with patch.object(Parser, 'parse') as mock_parse:
            self.parser.get_html_dict()
            mock_parse.assert_called_once()
    
    def test_type_line_returns_title(self):
        line = "title: This is a title"
        self.assertEqual(self.parser.type_line(line), 'title')
        
    def test_type_line_returns_category(self):
        line = "category: This is a category"
        self.assertEqual(self.parser.type_line(line), 'category')
        
    def test_type_line_returns_intro(self):
        line = "intro: This is an intro"
        self.assertEqual(self.parser.type_line(line), 'intro')
        
    def test_type_line_returns_code(self):
        line = "code: This is a code"
        self.assertEqual(self.parser.type_line(line), 'code')
        
    def test_type_line_returns_link(self):
        line = "link: This is a link"
        self.assertEqual(self.parser.type_line(line), 'link')
        
    def test_type_line_returns_title1(self):
        line = "# This is a title1"
        self.assertEqual(self.parser.type_line(line), 'title1')
        
    def test_type_line_returns_title2(self):
        line = "## This is a title2"
        self.assertEqual(self.parser.type_line(line), 'title2')
        
    def test_type_line_returns_title3(self):
        line = "### This is a title3"
        self.assertEqual(self.parser.type_line(line), 'title3')
        
    def test_type_line_returns_list(self):
        line = "list: papa, maman"
        self.assertEqual(self.parser.type_line(line), 'list')
    
    def test_type_line_returns_paragraph(self):
        line = "This is a paragraph"
        self.assertEqual(self.parser.type_line(line), 'paragraph')
        
    def test_type_line_returns_end(self):
        line = ""
        self.assertEqual(self.parser.type_line(line), 'end')    
                
    def test_parse_returns_dict(self):
        actual = self.parser.parse()
        expected = self.parser.html_dict
        self.assertEqual(actual, expected)
        
        
        
        
        
