# Generated by Django 4.0.5 on 2022-07-08 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_alter_article_content_alter_article_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='pic',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='url',
            field=models.URLField(max_length=255, null=True),
        ),
    ]
