# Generated by Django 2.2.5 on 2019-09-21 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='district_name_eng',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='district',
            name='district_name_mmr',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='township',
            name='township_name_eng',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='township',
            name='township_name_mmr',
            field=models.CharField(max_length=50),
        ),
    ]
