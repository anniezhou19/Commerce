# Generated by Django 4.0.3 on 2022-10-18 13:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_listing_isactive_alter_category_categoryname'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='watchlist',
            field=models.ManyToManyField(blank=True, null=True, related_name='Watchlisting', to=settings.AUTH_USER_MODEL),
        ),
    ]
