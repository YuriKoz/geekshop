# Generated by Django 3.2.11 on 2022-02-02 12:15

import datetime

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("authnapp", "0003_auto_20220202_1111"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shopuser",
            name="activation_key_expires",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 2, 4, 12, 15, 17, 549622, tzinfo=utc), verbose_name="актуальность ключа"
            ),
        ),
        migrations.CreateModel(
            name="ShopUserProfile",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("tagline", models.CharField(blank=True, max_length=128, verbose_name="теги")),
                ("aboutMe", models.TextField(blank=True, max_length=512, verbose_name="о себе")),
                (
                    "gender",
                    models.CharField(blank=True, choices=[("M", "М"), ("W", "Ж")], max_length=1, verbose_name="пол"),
                ),
                (
                    "user",
                    models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
                ),
            ],
        ),
    ]
