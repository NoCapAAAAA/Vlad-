# Generated by Django 4.0.5 on 2023-03-31 14:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_historyorders_remove_tirestore_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historyorders',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 31, 14, 59, 0, 168472, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='historyorders',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]