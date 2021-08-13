# Generated by Django 3.1 on 2021-07-31 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataapp', '0003_auto_20210731_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='unit_price',
            field=models.IntegerField(choices=[('Grade 1', ((230, 230),)), ('Grade 2', ((150, 150),))], default=150),
        ),
        migrations.AlterField(
            model_name='billing',
            name='year',
            field=models.IntegerField(choices=[(2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028), (2029, 2029), (2030, 2030)], default=2021),
        ),
    ]
