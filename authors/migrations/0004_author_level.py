# Generated by Django 3.1.3 on 2020-11-22 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0003_auto_20201121_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='level',
            field=models.CharField(choices=[('J', 'Junior'), ('M', 'Middle'), ('S', 'Senior')], default='J', max_length=1),
            preserve_default=False,
        ),
    ]
