# Generated by Django 4.2 on 2023-10-14 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_management', '0005_remove_slots_reservation_reservations_slot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slots',
            name='end_time',
            field=models.DateTimeField(blank=True, verbose_name='終了日時'),
        ),
    ]