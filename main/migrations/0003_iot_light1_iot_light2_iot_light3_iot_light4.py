# Generated by Django 4.1.7 on 2023-03-12 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_alter_iot_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="iot",
            name="light1",
            field=models.CharField(default=0, max_length=5, verbose_name="Влажность"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="iot",
            name="light2",
            field=models.CharField(default=0, max_length=5, verbose_name="Влажность"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="iot",
            name="light3",
            field=models.CharField(default=0, max_length=5, verbose_name="Влажность"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="iot",
            name="light4",
            field=models.CharField(default=0, max_length=5, verbose_name="Влажность"),
            preserve_default=False,
        ),
    ]
