"""mail views tests"""

from unittest.mock import patch

from article.models import Article, ArticleCategory, Category
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse


class TestMailMeView(TestCase):
    
    fixtures = [
        "category_fixture.json",
        "article_fixture.json",
        "user_fixture.json",
        "article_category_fixture.json"
    ]
    
    @staticmethod
    def create_user():
        username="papa"
        password="nimportequoi1938"
        email="papa@gmail.Com"
        
        return get_user_model().objects.create_user(
            username=username,
            email=email,
            password=password
        )
    
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.url = "mail_me"
        
    def setUp(self):
        self.create_user()
        self.client.login(email="papa@gmail.com", password="nimportequoi1938")
        
        
    def test_response_with_no_user_log(self):
        self.client.logout()
        response = self.client.get(reverse(self.url))
        self.assertTrue(response.status_code == 302)
        
    def test_response_with_user_log(self):
        response = self.client.get(reverse(self.url))
        self.assertTrue(response.status_code == 200)

    @patch("mail.views.send_mail")
    def test_response_if_send_mail_error(self, mock_send_mail):
        mock_send_mail.side_effect = Exception("Error")
        response = self.client.post(reverse(self.url), {
            "mail-object": "test",
            "mail-text": "test"
        })
        self.assertTrue(response.status_code == 200)
        self.assertTemplateUsed(response, "mail/mail_error.html")

    @patch("mail.views.send_mail")
    def test_response_if_send_mail_OK(self, mock_send_mail):
        mock_send_mail.return_value={}
        response = self.client.post(reverse(self.url), {
            "mail-object": "test",
            "mail-text": "test"
        })
        self.assertTrue(response.status_code == 200)
        self.assertTemplateUsed(response, "mail/mail_sent.html")


class TestOtherViews(TestCase):
    
    def setUp(self):
        self.client=Client()
        
    def test_mail_error_view(self):
        response = self.client.get(reverse("mail_error"))
        self.assertTrue(response.status_code == 200)
        self.assertTemplateUsed(response, "mail/mail_error.html")
        
    def test_mail_sent_view(self):
        response = self.client.get(reverse("mail_sent"))
        self.assertTrue(response.status_code == 200)
        self.assertTemplateUsed(response, "mail/mail_sent.html")
