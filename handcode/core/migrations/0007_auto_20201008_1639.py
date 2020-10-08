# Generated by Django 3.1.1 on 2020-10-08 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20201008_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='github',
            field=models.URLField(blank=True, verbose_name='GitHub'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='instagram',
            field=models.URLField(blank=True, verbose_name='Instagram'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='linkdin',
            field=models.URLField(blank=True, verbose_name='Linkedin'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
    ]
