# Generated by Django 4.1.7 on 2023-03-06 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="IoT",
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
                ("tempre", models.CharField(max_length=10, verbose_name="Температура")),
                ("gas", models.CharField(max_length=10, verbose_name="СО2")),
                ("punch", models.CharField(max_length=10, verbose_name="Удры")),
                ("liq", models.CharField(max_length=10, verbose_name="Влажность")),
            ],
        ),
    ]