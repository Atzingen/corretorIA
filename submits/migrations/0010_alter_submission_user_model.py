# Generated by Django 4.0 on 2022-01-02 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('submits', '0009_alter_notas_user_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='user_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
