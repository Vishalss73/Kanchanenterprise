# Generated by Django 4.2.2 on 2023-06-26 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enterpriseapp', '0015_contact_details_phonenumber_emailaddress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailaddress',
            name='Contact_details',
        ),
        migrations.DeleteModel(
            name='Home',
        ),
        migrations.RemoveField(
            model_name='phonenumber',
            name='Contact_details',
        ),
        migrations.DeleteModel(
            name='Contact_details',
        ),
        migrations.DeleteModel(
            name='EmailAddress',
        ),
        migrations.DeleteModel(
            name='PhoneNumber',
        ),
    ]