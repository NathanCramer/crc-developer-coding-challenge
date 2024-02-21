# Generated by Django 5.0.2 on 2024-02-21 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_participant_age_remove_participant_bmi_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='participant',
            name='surname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='participantworkout',
            name='score',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='workout',
            name='description',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='workout',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]