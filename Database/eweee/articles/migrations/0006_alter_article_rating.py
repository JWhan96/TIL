# Generated by Django 4.2.5 on 2023-10-13 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_article_genre_article_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='rating',
            field=models.CharField(max_length=10),
        ),
    ]