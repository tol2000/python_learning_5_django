# Generated by Django 3.1.3 on 2020-11-22 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0004_author_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(blank='none@none.no', default='none@none.no', max_length=254, null=True),
        ),
    ]
