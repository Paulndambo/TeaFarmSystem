# Generated by Django 3.1 on 2021-07-31 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataapp', '0004_auto_20210731_2344'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billing',
            old_name='quantity',
            new_name='total_quantity_delivered',
        ),
        migrations.RemoveField(
            model_name='billing',
            name='unit_price',
        ),
    ]