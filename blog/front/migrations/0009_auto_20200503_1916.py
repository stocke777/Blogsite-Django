# Generated by Django 2.2.5 on 2020-05-03 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0008_auto_20200503_1915'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author_id',
            new_name='author',
        ),
    ]
