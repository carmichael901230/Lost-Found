# Generated by Django 2.2 on 2019-06-08 19:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0008_auto_20190608_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='date',
            field=models.DateField(blank=True, default=datetime.date(2019, 6, 8), null=True),
        ),
    ]