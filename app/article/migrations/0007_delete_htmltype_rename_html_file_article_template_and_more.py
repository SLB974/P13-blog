# Generated by Django 4.0.5 on 2022-07-22 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_article_html_file_alter_article_url_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HtmlType',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='html_file',
            new_name='template',
        ),
        migrations.RemoveField(
            model_name='article',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='article',
            name='url',
        ),
    ]
