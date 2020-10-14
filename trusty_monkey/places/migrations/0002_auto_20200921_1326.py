# Generated by Django 3.0.8 on 2020-09-21 13:26

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='website',
            field=models.CharField(blank=True, max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='opened',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=1200, null=True), size=None),
        ),
    ]
