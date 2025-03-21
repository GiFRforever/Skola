# Generated by Django 4.2.1 on 2023-05-23 08:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="article",
            name="published_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="article",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
