# Generated by Django 4.0 on 2022-01-02 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('submits', '0006_profile_info_delete_notas_delete_submission'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.FloatField()),
                ('atividade', models.IntegerField()),
                ('user_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='submits.profile_info')),
            ],
        ),
    ]