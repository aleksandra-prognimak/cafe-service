# Generated by Django 4.1 on 2024-04-08 19:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0003_alter_dish_dish_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cook',
            name='years_of_experience',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(80)]),
        ),
    ]