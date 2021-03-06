# Generated by Django 4.0.2 on 2022-03-04 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='is_mapper',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='MapModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_x', models.CharField(max_length=10)),
                ('a_y', models.CharField(max_length=10)),
                ('b_x', models.CharField(max_length=10)),
                ('b_y', models.CharField(max_length=10)),
                ('c_x', models.CharField(max_length=10)),
                ('c_y', models.CharField(max_length=10)),
                ('d_x', models.CharField(max_length=10)),
                ('d_z', models.CharField(max_length=10)),
                ('area', models.CharField(max_length=10)),
                ('x', models.CharField(max_length=10)),
                ('y', models.CharField(max_length=10)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.mapimage')),
            ],
        ),
        migrations.AddField(
            model_name='mapimage',
            name='map_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.user'),
        ),
    ]
