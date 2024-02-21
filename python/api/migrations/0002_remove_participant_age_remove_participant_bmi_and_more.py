# Generated by Django 5.0.2 on 2024-02-21 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='age',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='bmi',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='height',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='weight',
        ),
        migrations.AddField(
            model_name='participant',
            name='surname',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
