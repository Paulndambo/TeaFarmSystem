# Generated by Django 3.1 on 2021-08-12 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataapp', '0013_auto_20210812_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='year',
            field=models.IntegerField(default=2021, editable=False),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='join_year',
            field=models.IntegerField(default=2021, editable=False),
        ),
        migrations.AlterField(
            model_name='payfarmer',
            name='year',
            field=models.IntegerField(default=2021, editable=False),
        ),
    ]
