# Generated by Django 2.2 on 2019-06-06 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_auto_20190606_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]