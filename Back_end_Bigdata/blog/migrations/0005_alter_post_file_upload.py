# Generated by Django 4.0.4 on 2022-05-18 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_file_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file_upload',
            field=models.FileField(blank=True, upload_to='blog/files/%Y/%m/%d/'),
        ),
    ]
