# Generated by Django 3.1.3 on 2020-11-26 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0004_article_publisher'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Publisher',
        ),
    ]
