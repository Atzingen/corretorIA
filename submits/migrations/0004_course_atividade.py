# Generated by Django 4.0 on 2022-03-09 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('submits', '0003_alter_user_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('short_description', models.CharField(max_length=500)),
                ('long_description', models.CharField(max_length=2000)),
                ('requeriments', models.CharField(max_length=500)),
                ('year', models.IntegerField()),
                ('semester', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('active', models.BooleanField()),
                ('inscriptions_open', models.BooleanField()),
                ('youtube', models.CharField(max_length=100)),
                ('github', models.CharField(max_length=100)),
                ('student', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_description', models.CharField(max_length=500)),
                ('long_description', models.CharField(max_length=2000)),
                ('nome', models.CharField(max_length=500)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('tags', models.CharField(max_length=500)),
                ('receiving_submissions', models.BooleanField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='submits.course')),
            ],
        ),
    ]
