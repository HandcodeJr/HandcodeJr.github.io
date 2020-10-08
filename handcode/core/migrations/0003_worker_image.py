# Generated by Django 3.1.1 on 2020-10-08 18:17

import core.models
from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201008_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='image',
            field=stdimage.models.StdImageField(default=0, upload_to=core.models.get_file_path, verbose_name='Imagem'),
            preserve_default=False,
        ),
    ]
