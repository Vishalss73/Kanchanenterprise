# Generated by Django 4.2.2 on 2023-06-27 05:01

from django.db import migrations
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('enterpriseapp', '0024_service_publisher_morebenifit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='service_publisher',
            name='bottomparagraph',
            field=tinymce.models.HTMLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
