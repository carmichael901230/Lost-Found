# Generated by Django 2.2 on 2019-06-08 19:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0010_auto_20190608_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]