# Generated by Django 4.1 on 2022-08-26 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_remove_doctor_spaciality'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='label',
        ),
    ]
