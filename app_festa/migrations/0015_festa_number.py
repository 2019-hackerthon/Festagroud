# Generated by Django 2.2.3 on 2019-07-27 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_festa', '0014_merge_20190728_0011'),
    ]

    operations = [
        migrations.AddField(
            model_name='festa',
            name='number',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.CASCADE, to='app_festa.RegisterNum'),
            preserve_default=False,
        ),
    ]
