# Generated by Django 2.2.5 on 2020-05-03 13:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0007_post_author_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
