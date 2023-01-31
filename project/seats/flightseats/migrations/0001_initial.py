# Generated by Django 4.1.5 on 2023-01-31 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_choice', models.CharField(default='none', max_length=30, unique=True)),
                ('reserved_by', models.CharField(default='none', max_length=30)),
                ('booking_time', models.CharField(default='none', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=0)),
                ('month', models.IntegerField(default=0)),
                ('day', models.IntegerField(default=0)),
                ('airline', models.CharField(default='Airline', max_length=250)),
                ('flight_number', models.IntegerField(default=0)),
                ('origin_airport', models.CharField(default='Airport', max_length=250)),
                ('dest_airport', models.CharField(default='destination', max_length=250)),
                ('departure', models.CharField(default='Time', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Seats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_row_number', models.CharField(default='1', max_length=250)),
                ('column_a', models.CharField(default='A', max_length=250)),
                ('column_b', models.CharField(default='B', max_length=250)),
                ('column_c', models.CharField(default='C', max_length=250)),
                ('column_d', models.CharField(default='D', max_length=250)),
                ('column_e', models.CharField(default='E', max_length=250)),
                ('column_f', models.CharField(default='F', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'Statistics page',
            },
        ),
    ]
