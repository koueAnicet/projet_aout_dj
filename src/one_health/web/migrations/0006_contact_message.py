# Generated by Django 4.1 on 2022-08-26 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_alter_about_title_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.TextField(default='hello comment tu va'),
            preserve_default=False,
        ),
    ]
