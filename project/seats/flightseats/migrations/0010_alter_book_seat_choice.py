# Generated by Django 4.1.4 on 2023-01-16 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightseats', '0009_remove_book_airline_book_seat_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='seat_choice',
            field=models.CharField(default='none', max_length=30),
        ),
    ]