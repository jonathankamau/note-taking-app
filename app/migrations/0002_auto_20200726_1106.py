# Generated by Django 3.0.8 on 2020-07-26 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetingcategory',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='purpose',
            field=models.TextField(blank=True),
        ),
    ]
