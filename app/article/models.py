from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category

class Article(models.Model):
    title = models.CharField(max_length=255)
    tuto = models.BooleanField(default=False)
    content = models.TextField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    url=models.URLField(max_length=255)

    def __str__(self):
        return self.title
