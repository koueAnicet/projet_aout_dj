# Generated by Django 4.1 on 2022-08-25 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_sociallink_icon_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='title_about',
            field=models.CharField(max_length=150),
        ),
    ]
