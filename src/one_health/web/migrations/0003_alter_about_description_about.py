# Generated by Django 4.0.5 on 2022-08-25 12:53

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_banner_about_active_contact_active_siteinfos_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='description_about',
            field=tinymce.models.HTMLField(),
        ),
    ]