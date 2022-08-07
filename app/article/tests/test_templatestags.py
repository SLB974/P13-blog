from article.templatetags.home_extras import get_details
from django.test import TestCase, client


class TestTemplatesTags(TestCase):
    
    fixtures = [
    'article_category_fixture.json',
    'article_fixture.json',
    'category_fixture.json',
    ]
    
    def setUp(self):
        self.client = client.Client()

    def test_get_details_category(self):
        response = get_details('category')
        self.assertEqual(response,'(3)')
        
    def test_get_details_article(self):
        response = get_details('article')
        self.assertEqual(response,'(2)')
        
    def test_get_details_tuto(self):
        response = get_details('tuto')
        self.assertEqual(response,'(1)')
        
    def test_get_details_oops(self):
        response = get_details('oops')
        self.assertEqual(response,'(1)')

    def test_get_details_other(self):
        response = get_details('')
        self.assertEqual(response,'')
