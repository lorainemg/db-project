# Generated by Django 2.1 on 2018-10-31 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_auto_20181031_0335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='date_start',
            field=models.DateField(unique_for_year=True, verbose_name='fecha inicio'),
        ),
    ]
