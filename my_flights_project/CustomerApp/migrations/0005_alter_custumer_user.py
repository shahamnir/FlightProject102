# Generated by Django 4.2.1 on 2023-06-03 14:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CustomerApp', '0004_alter_custumer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custumer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
