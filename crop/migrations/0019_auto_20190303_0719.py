# Generated by Django 2.1.3 on 2019-03-03 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0018_buyer_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='date_time',
        ),
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
