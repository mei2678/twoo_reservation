# Generated by Django 4.2 on 2023-10-09 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking_management', '0003_slots'),
    ]

    operations = [
        migrations.AddField(
            model_name='slots',
            name='reservation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='slots_reservatioins', to='booking_management.reservations', verbose_name='予約'),
        ),
    ]
