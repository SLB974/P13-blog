# Generated by Django 4.0.5 on 2022-07-05 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='oops',
            field=models.BooleanField(default=False),
        ),
    ]