# Generated by Django 4.0.1 on 2022-05-19 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_file_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hook_text',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
