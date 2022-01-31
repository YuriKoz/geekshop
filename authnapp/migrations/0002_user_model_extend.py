# Generated by Django 3.2.11 on 2022-01-31 11:53

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("authnapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="shopuser",
            name="activation_key",
            field=models.CharField(blank=True, max_length=128, verbose_name="ключ подтверждения"),
        ),
        migrations.AddField(
            model_name="shopuser",
            name="activation_key_expires",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 2, 2, 11, 53, 37, 287086, tzinfo=utc), verbose_name="актуальность ключа"
            ),
        ),
    ]
