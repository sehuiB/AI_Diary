# Generated by Django 5.1.3 on 2024-11-22 07:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_app", "0003_diary"),
    ]

    operations = [
        migrations.AddField(
            model_name="diary",
            name="image_path",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
