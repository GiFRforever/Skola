# Generated by Django 4.2.1 on 2023-05-23 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0003_article_highlight_article_picture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="picture",
            field=models.ImageField(
                blank=True, null=True, upload_to="media/article_pictures"
            ),
        ),
    ]
