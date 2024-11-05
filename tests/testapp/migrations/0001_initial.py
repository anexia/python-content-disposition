# Generated by Django 3.2.13 on 2022-06-15 11:53

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Photo",
            fields=[
                (
                    "name",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                (
                    "file",
                    models.FileField(
                        max_length=255,
                        upload_to="photos/uploads/bb50c426-eca1-11ec-b3a2-f7680d273bc6",
                        verbose_name="file",
                    ),
                ),
                ("mime", models.CharField(max_length=256, verbose_name="mime")),
            ],
        ),
    ]
