# Generated by Django 2.2.5 on 2019-09-21 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0003_auto_20190922_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='township',
            name='source',
            field=models.CharField(max_length=20),
        ),
    ]
