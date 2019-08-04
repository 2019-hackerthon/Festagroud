# Generated by Django 2.2.3 on 2019-08-04 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_festaNow', '0004_auto_20190801_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='post_type',
            field=models.CharField(choices=[('중요', '중요'), ('질문', '질문')], default='중요', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='home',
            name='region',
            field=models.CharField(choices=[('서울', '서울'), ('경기', '경기'), ('제주', '제주')], max_length=200),
        ),
    ]