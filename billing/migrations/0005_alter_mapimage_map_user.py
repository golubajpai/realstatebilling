# Generated by Django 4.0.2 on 2022-03-04 07:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0004_alter_mapimage_map_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapimage',
            name='map_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to=settings.AUTH_USER_MODEL),
        ),
    ]
