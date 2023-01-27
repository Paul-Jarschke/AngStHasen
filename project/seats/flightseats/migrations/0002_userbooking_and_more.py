# Generated by Django 4.1.5 on 2023-01-27 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightseats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_choice', models.CharField(default='none', max_length=30, unique=True)),
                ('reserved_by', models.CharField(default='none', max_length=30)),
            ],
        ),
        migrations.RenameField(
            model_name='seats',
            old_name='column_rownumber',
            new_name='column_row_number',
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='empty', max_length=250),
        ),
    ]