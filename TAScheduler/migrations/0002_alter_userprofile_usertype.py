# Generated by Django 4.0 on 2021-12-09 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TAScheduler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='userType',
            field=models.CharField(choices=[('SUPERVISOR', 'Supervisor'), ('INSTRUCTOR', 'Instructor'), ('TA', 'TA')], max_length=20),
        ),
    ]
