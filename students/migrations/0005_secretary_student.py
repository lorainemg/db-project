# Generated by Django 2.1 on 2018-09-28 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_career_classroom_secretary'),
    ]

    operations = [
        migrations.AddField(
            model_name='secretary',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete='CASCADE', to='students.Student'),
        ),
    ]
