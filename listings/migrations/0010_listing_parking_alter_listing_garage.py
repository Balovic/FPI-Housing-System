# Generated by Django 4.2.6 on 2023-11-05 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0009_alter_listing_sqft'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='parking',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='listing',
            name='garage',
            field=models.BooleanField(default=False),
        ),
    ]
