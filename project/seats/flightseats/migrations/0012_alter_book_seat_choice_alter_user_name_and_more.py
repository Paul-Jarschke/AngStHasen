# Generated by Django 4.1.5 on 2023-01-21 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightseats', '0011_seats2_rows'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='seat_choice',
            field=models.CharField(default='none', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='empty', max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(default='empty', max_length=250, unique=True),
        ),
    ]
