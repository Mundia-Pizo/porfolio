# Generated by Django 2.2.5 on 2019-12-05 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_mywork_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='position',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
