# Generated by Django 2.2.7 on 2019-11-17 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_habit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]