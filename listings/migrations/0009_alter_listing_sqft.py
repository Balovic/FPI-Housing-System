# Generated by Django 4.2.6 on 2023-11-04 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_alter_city_properties_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='sqft',
            field=models.IntegerField(default=0),
        ),
    ]