from django.test import SimpleTestCase
from django.urls import resolve, reverse
from home import views


class TestHomeUrls(SimpleTestCase):
    def test_home_url_resolves(self):
        url = reverse("home")
        self.assertEqual(resolve(url).func, views.index)
