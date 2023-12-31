# Generated by Django 4.2 on 2023-10-14 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking_management', '0004_slots_reservation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slots',
            name='reservation',
        ),
        migrations.AddField(
            model_name='reservations',
            name='slot',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='booking_management.slots', verbose_name='予約枠'),
        ),
    ]
