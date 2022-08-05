"""testing mail urls"""

from django.test import SimpleTestCase
from django.urls import resolve, reverse
from mail import views


class TestMailUrls(SimpleTestCase):
    def test_send_mail_url_resolves(self):
        url = reverse("mail_me")
        self.assertEqual(resolve(url).func, views.mail_me)
    def test_mail_sent_url_resolves(self):
        url = reverse("mail_sent")
        self.assertEqual(resolve(url).func, views.mail_sent)
    def test_mail_error_url_resolves(self):
        url = reverse("mail_error")
        self.assertEqual(resolve(url).func, views.mail_error)
