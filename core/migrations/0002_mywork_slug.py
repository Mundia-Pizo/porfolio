# Generated by Django 2.2.5 on 2019-12-04 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mywork',
            name='slug',
            field=models.SlugField(default='none'),
            preserve_default=False,
        ),
    ]
