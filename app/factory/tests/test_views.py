import os

from django.test import Client, TestCase
from django.urls import reverse


class TestFactoryViews(TestCase):
    "testing factory views"
    
    def setUp(self):
        self.client = Client()
        
    def test_upload_md_file_view_response(self):
        response = self.client.get(reverse('upload'))
        self.assertEqual(response.status_code,200)
