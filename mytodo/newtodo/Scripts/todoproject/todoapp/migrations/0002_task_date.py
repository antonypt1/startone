# Generated by Django 4.2.6 on 2023-12-04 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1999-12-11'),
            preserve_default=False,
        ),
    ]
