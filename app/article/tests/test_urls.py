"""testing article urls"""

from article import views
from django.test import SimpleTestCase
from django.urls import resolve, reverse


class TestArticleUrls(SimpleTestCase):
        def test_category_list_url_resolves(self):
            url = reverse("category_list")
            self.assertEqual(resolve(url).func, views.category_list)

        def test_category_url_resolves(self):
            url = reverse("category", kwargs={"category": "python"})
            self.assertEqual(resolve(url).func, views.category)

        def test_article_list_url_resolves(self):
            url = reverse("article_list")
            self.assertEqual(resolve(url).func, views.article_list)
            
        def test_article_url_resolves(self):
            url = reverse("article", kwargs={"title": "python"})
            self.assertEqual(resolve(url).func, views.article)    
            
        def test_tuto_list_url_resolves(self):
            url = reverse("tuto_list")
            self.assertEqual(resolve(url).func, views.tuto_list)
            
        def test_delete_url_resolves(self):
            url = reverse("delete_article", kwargs={"title": "python"})
            self.assertEqual(resolve(url).func, views.delete)
            
        def test_oops_list_url_resolves(self):
            url = reverse("oops_list")
            self.assertEqual(resolve(url).func, views.oops_list)
            
            