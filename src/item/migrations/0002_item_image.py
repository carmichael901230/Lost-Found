# Generated by Django 2.2 on 2019-05-29 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img/%Y/%m/%d/'),
        ),
    ]