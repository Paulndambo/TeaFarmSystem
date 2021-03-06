# Generated by Django 3.1.5 on 2021-08-04 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataapp', '0005_auto_20210801_0016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billing',
            old_name='total_amount_owed',
            new_name='amount_paid',
        ),
        migrations.AddField(
            model_name='billing',
            name='balance',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='billing',
            name='pay',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='billing',
            name='total_cumulative_amount',
            field=models.FloatField(default=0),
        ),
    ]
