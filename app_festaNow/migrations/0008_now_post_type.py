# Generated by Django 2.2.3 on 2019-08-04 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_festaNow', '0007_team_post_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='now',
            name='post_type',
            field=models.CharField(choices=[('now', 'now'), ('질문', '질문'), ('나눔', '나눔')], default='질문', max_length=100),
            preserve_default=False,
        ),
    ]
