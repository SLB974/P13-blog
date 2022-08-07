from unittest.mock import patch

from django.test import TestCase
from factory.core.article_creator import ArticleCreator


class TestArticleCreator(TestCase):
    
    fixtures = [
        'category_fixture.json'
    ]
    
    def setUp(self):
        self.html_dict = {
            "title": "This is a title",
            "category": ["Python", "Docker"],
            "intro": "This is an intro",
            "content": [("paragraph", "This is a paragraph")]       
            }
        self.html_file = "test.html"
        self.creator = ArticleCreator(self.html_dict, self.html_file)
        
    
    def test_get_tuto_returns_false(self):
        self.assertFalse(self.creator.get_tuto())
        
    def test_get_oops_returns_false(self):
        self.assertFalse(self.creator.get_oops())
        
    def test_check_article_returns_false(self):
        self.assertFalse(self.creator.check_article())
        
    @patch('factory.tests.tests_article_creator.ArticleCreator.create_category')
    def test_append_database_calls_create_category(self, mock):
        try:
            self.creator.append_database()
        except Exception:
            pass
        mock.assert_called_once()
        
    @patch('factory.tests.tests_article_creator.ArticleCreator.create_article')
    def test_append_database_calls_create_article(self, mock):
        try:
            self.creator.append_database()
        except Exception:
            pass
        mock.assert_called_once()
        
    @patch('factory.tests.tests_article_creator.ArticleCreator.create_article_category')
    def test_append_database_calls_create_article_category(self, mock):
        try:
            self.creator.append_database()
        except Exception:
            pass
        mock.assert_called_once()
        
        
    