# Generated by Django 3.1.3 on 2020-11-26 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0008_article_publisher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='body',
        ),
    ]