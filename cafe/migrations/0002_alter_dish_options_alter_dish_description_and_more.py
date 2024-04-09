# Generated by Django 4.1 on 2024-02-27 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("cafe", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="dish",
            options={"verbose_name_plural": "dishes"},
        ),
        migrations.AlterField(
            model_name="dish",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="dish",
            name="dish_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="cafe.dishtype"
            ),
        ),
    ]
