# Generated by Django 4.1.5 on 2023-01-26 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cnab",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("type", models.CharField(max_length=21)),
                ("data", models.CharField(max_length=24)),
                ("value", models.IntegerField()),
                ("cpf", models.CharField(max_length=11)),
                ("card", models.CharField(max_length=24)),
                ("hour", models.CharField(max_length=24)),
                ("owner", models.CharField(max_length=64)),
                ("shop", models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name="Upload",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("file", models.FileField(upload_to="uploads")),
            ],
        ),
    ]
