# Generated by Django 2.2.6 on 2020-06-09 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pancar', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='car',
        ),
        migrations.AddField(
            model_name='car',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
