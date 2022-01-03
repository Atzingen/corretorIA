# Generated by Django 4.0 on 2022-01-02 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('submits', '0005_remove_notas_nota_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('user_model', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.DeleteModel(
            name='Notas',
        ),
        migrations.DeleteModel(
            name='Submission',
        ),
    ]