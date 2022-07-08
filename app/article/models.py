from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=255)
    pic=models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.category

class Article(models.Model):
    title = models.CharField(max_length=255)
    tuto = models.BooleanField(default=False)
    oops=models.BooleanField(default=False)
    content = models.TextField(null=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    url=models.URLField(max_length=255, null=True)

    def __str__(self):
        return self.title
