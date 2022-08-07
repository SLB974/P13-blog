from article.models import Article, Category
from django.test import Client, TestCase
from django.urls import reverse


class TestCategoryModel(TestCase):
    """testing Category Model"""
    
    fixtures = [
        'article_category_fixture.json',
        'article_fixture.json',
        'category_fixture.json',
    ]

    def setUp(self):
        self.client = Client()
        
    def test_str_returns_name(self):
        response = Category.objects.get(category='Python').__str__()
        expected = 'Python'
        self.assertTrue(response, expected)

    def test_exists_returns_true_with_Python(self):
        response = Category.exists('Python')
        self.assertTrue(response)

    def test_exists_returns_false_with_Java(self):
        response = Category.exists('Java')
        self.assertFalse(response)

    def test_get_count_returns_3(self):
        response = Category.get_count()
        self.assertEqual(response, 3)

    def test_get_item_returns_proper_value(self):
        actual = Category.get_item('Python')
        expected = 'Python'
        self.assertTrue(actual, expected)
        
    def test_get_related_articles_returns_proper_value(self):
        actual = Category.get_related_articles('Python')
        expected = Category.objects.get(category='Python').categories.all()
        self.assertTrue(actual, expected)

    def test_add_item_when_item_exists_returns_item(self):
        category = Category()
        actual = category.add_item('Python')
        expected = 'Python'
        self.assertTrue(actual, expected)

    def test_add_item_when_item_does_not_exists(self):
        category = Category()
        actual = category.add_item('papa')
        expected = 'papa'
        self.assertTrue(actual, expected)

class TestArticleModel(TestCase):
    """testing Article Model"""
    
    fixtures = [
        'article_category_fixture.json',
        'article_fixture.json',
        'category_fixture.json',
    ]

    def setUp(self):
        self.client = Client()
        
    def test_str_returns_title(self):
        response = Article.objects.get(title='Récursion en Python').__str__()
        expected = 'Récursion en Python'
        self.assertTrue(response, expected)

    def test_get_count_returns_2(self):
        response = Article.get_count()
        self.assertEqual(response, 2)

    def test_exists_return_true_with_Récursion_en_Python(self):
        response = Article.exists('Récursion en Python')
        self.assertTrue(response)
        
    def test_exists_returns_false_with_Récursion_en_Java(self):
        response = Article.exists('Récursion en Java')
        self.assertFalse(response)

    def add_item_returns_existing_article_if_exists(self):
        article=Article()
        response = article.add_item('Récursion en Python')
        self.assertTrue(response, 'Récursion en Python')
        
    def add_item_returns_new_article_if_does_not_exists(self):
        article=Article()
        response = article.add_item('Récursion en Java')
        self.assertTrue(response, 'Récursion en Java')

