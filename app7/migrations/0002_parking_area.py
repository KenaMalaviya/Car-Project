# Generated by Django 4.1.6 on 2023-05-01 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app7', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='parking_area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parking_name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('zipcode', models.IntegerField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
    ]
