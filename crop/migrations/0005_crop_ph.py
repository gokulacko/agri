# Generated by Django 2.1.3 on 2019-02-28 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0004_auto_20190228_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='crop',
            name='ph',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crop.Ph'),
        ),
    ]