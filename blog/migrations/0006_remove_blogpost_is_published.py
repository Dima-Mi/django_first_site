# Generated by Django 3.1.3 on 2020-11-05 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20201105_1100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='is_published',
        ),
    ]