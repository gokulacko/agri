# Generated by Django 2.1.3 on 2019-03-02 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0008_auto_20190301_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='land',
            name='ph',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True),
        ),
    ]