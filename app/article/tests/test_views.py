"""article views tests"""

import os

from django.test import Client, TestCase
from django.urls import reverse


class TestArticleViews(TestCase):
    """testing article views"""
    
    fixtures = [
        'article_category_fixture.json',
        'article_fixture.json',
        'category_fixture.json',
        'user_fixture.json',
    ]

    def setUp(self):
        self.client = Client()
        
    def tearDown(self):
        if os.path.exists("mediafiles/generated_templates/test.html"):
            os.remove("mediafiles/generated_templates/test.html")
        
    def create_test_html_file(self):
        file = "mediafiles/generated_templates/test.html"
        open(file,'a').close()

        
    def test_category_list_view_response(self):
        response = self.client.get(reverse('category_list'))
        self.assertEqual(response.status_code,200)

    def test_category_view_response(self):
        response = self.client.get(reverse('category', args=['python']))
        self.assertEqual(response.status_code,200)

    def test_article_list_view_response(self):
        response = self.client.get(reverse('article_list'))
        self.assertEqual(response.status_code,200)

    def test_tuto_list_view_response(self):
        response = self.client.get(reverse('tuto_list'))
        self.assertEqual(response.status_code,200)
        
    def test_oops_list_view_response(self):
        response = self.client.get(reverse('oops_list'))
        self.assertEqual(response.status_code,200)
        
    def test_article_view_response(self):
        self.create_test_html_file()
        response = self.client.get(reverse('article', args=['Récursion en Python']))
        self.assertEqual(response.status_code,200)
    
    def test_article_delete_view_response(self):
        self.create_test_html_file()
        response = self.client.get(reverse('delete_article', args=['Récursion en Python']))
        self.assertEqual(response.status_code,302)
