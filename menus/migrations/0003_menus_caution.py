# Generated by Django 4.2 on 2023-09-10 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0002_cautions'),
    ]

    operations = [
        migrations.AddField(
            model_name='menus',
            name='caution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='menus.cautions'),
        ),
    ]