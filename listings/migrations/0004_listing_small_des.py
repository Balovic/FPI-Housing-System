# Generated by Django 4.2.6 on 2023-11-04 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_remove_listing_list_date_listing_date_added_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='small_des',
            field=models.CharField(default=2023, max_length=200),
            preserve_default=False,
        ),
    ]