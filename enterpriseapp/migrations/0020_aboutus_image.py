# Generated by Django 4.2.2 on 2023-06-26 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterpriseapp', '0019_rename_about_aboutus'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]