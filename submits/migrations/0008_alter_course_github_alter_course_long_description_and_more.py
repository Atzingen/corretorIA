# Generated by Django 4.0 on 2022-04-15 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submits', '0007_alter_activity_errata_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='github',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='long_description',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='requeriments',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='debug_data',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
