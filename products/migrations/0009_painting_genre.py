# Generated by Django 3.1 on 2020-08-27 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20200826_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='painting',
            name='genre',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
