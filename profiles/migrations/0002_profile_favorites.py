# Generated by Django 3.1.5 on 2021-01-06 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='favorites',
            field=models.ManyToManyField(blank=True, related_name='favorited_by', to='articles.Article'),
        ),
    ]
