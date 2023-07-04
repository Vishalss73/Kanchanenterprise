# Generated by Django 4.2.2 on 2023-06-26 07:52

from django.db import migrations, models
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('enterpriseapp', '0013_rename_village_dist_ongoingproject_dist_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='home',
            name='meta_discription',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='home',
            name='copyright',
            field=tinymce.models.HTMLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]