# Generated by Django 2.2.3 on 2019-07-25 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_festa', '0008_auto_20190723_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registernum',
            name='register_num',
            field=models.CharField(max_length=10),
        ),
    ]
