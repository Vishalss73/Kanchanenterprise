# Generated by Django 4.2.2 on 2023-06-22 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enterpriseapp', '0012_ongoingproject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ongoingproject',
            old_name='village_dist',
            new_name='dist',
        ),
        migrations.RenameField(
            model_name='ongoingproject',
            old_name='village_tall',
            new_name='tall',
        ),
    ]
