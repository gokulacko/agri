# Generated by Django 2.1.3 on 2019-03-02 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0010_land_pincode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='land',
            name='area',
        ),
        migrations.RemoveField(
            model_name='land',
            name='stability',
        ),
    ]
