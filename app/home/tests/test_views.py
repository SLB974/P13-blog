"""factory views tests"""

from django.test import Client, TestCase
from django.urls import reverse


class TestFactoryViews(TestCase):
    """testing factory views"""
    
    def setUp(self):
        self.client = Client()
        
    def test_index_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code,200)
        