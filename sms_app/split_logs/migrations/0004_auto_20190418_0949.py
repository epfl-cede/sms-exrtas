# Generated by Django 2.2 on 2019-04-18 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('split_logs', '0003_auto_20190418_0801'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileoriginal',
            name='lines_error',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='fileoriginal',
            name='lines_total',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
