# Generated by Django 4.2.2 on 2023-06-26 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterpriseapp', '0020_aboutus_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='backgroundimage',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]