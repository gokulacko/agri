# Generated by Django 2.1.3 on 2019-03-03 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0015_auto_20190303_0530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='expected_price',
            field=models.IntegerField(),
        ),
    ]