# Generated by Django 5.0.6 on 2024-09-16 14:13

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0004_blog"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="cover_img",
            field=models.ImageField(null=True, upload_to=app.models.Blog.upload_to),
        ),
    ]