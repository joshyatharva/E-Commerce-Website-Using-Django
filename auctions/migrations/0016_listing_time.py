# Generated by Django 3.0.9 on 2020-08-15 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_listing_ncomments'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
