# Generated by Django 4.0.2 on 2022-02-10 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0001_initial'),
        ('jwt_auth', '0004_user_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='city',
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='jwt_auth', to='city.city'),
            preserve_default=False,
        ),
    ]