# Generated by Django 4.0 on 2022-01-11 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, default='avatar128.png', upload_to='profile'),
        ),
    ]
