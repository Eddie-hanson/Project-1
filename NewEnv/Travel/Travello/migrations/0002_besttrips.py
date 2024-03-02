# Generated by Django 4.1.13 on 2024-03-01 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travello', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bestTrips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dest', models.CharField(max_length=100)),
                ('day', models.IntegerField()),
                ('month', models.CharField(max_length=15)),
                ('desc', models.TextField()),
                ('img', models.ImageField(upload_to='pic')),
            ],
        ),
    ]
