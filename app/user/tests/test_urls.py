"""testing user urls"""

from django.test import SimpleTestCase
from django.urls import resolve, reverse
from user import views


class TestUserUrls(SimpleTestCase):
    def test_signup_url_resolves(self):
        url = reverse("signup")
        self.assertEqual(resolve(url).func, views.signup)
