# Generated by Django 3.1 on 2021-08-12 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataapp', '0012_auto_20210812_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payfarmer',
            name='year',
            field=models.IntegerField(choices=[(2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028), (2029, 2029), (2030, 2030)]),
        ),
    ]
