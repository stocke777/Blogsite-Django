# Generated by Django 2.2.5 on 2020-05-03 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0005_auto_20200503_1912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author_id',
        ),
    ]