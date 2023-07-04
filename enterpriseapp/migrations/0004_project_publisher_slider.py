# Generated by Django 4.2.2 on 2023-06-21 09:32

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterpriseapp', '0003_alter_post_slug_pages_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project_publisher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('projectimage', models.ImageField(blank=True, null=True, upload_to='images')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('discription', ckeditor.fields.RichTextField()),
                ('heading', models.CharField(blank=True, max_length=255, null=True)),
                ('headingdiscription', ckeditor.fields.RichTextField()),
                ('smallfirstimg', models.ImageField(blank=True, null=True, upload_to='images')),
                ('smallsecondimg', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('smalltitle', models.CharField(max_length=255, null=True)),
                ('bigtitle', models.CharField(max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('imagealt', models.CharField(blank=True, max_length=255, null=True)),
                ('discription', models.CharField(max_length=1000, null=True)),
                ('link', models.CharField(max_length=254, null=True)),
            ],
        ),
    ]
