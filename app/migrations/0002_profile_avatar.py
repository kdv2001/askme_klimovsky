# Generated by Django 3.2.8 on 2021-11-10 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='/static/img/chaplin.jpg', max_length=64, upload_to=''),
        ),
    ]