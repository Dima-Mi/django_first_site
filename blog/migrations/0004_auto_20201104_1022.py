# Generated by Django 3.1.3 on 2020-11-04 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_blogpost_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='slug',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photo/%Y/%m/%d'),
        ),
    ]
