# Generated by Django 4.2 on 2023-11-06 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_management', '0006_customuser_name_customuser_namekana'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='namekana',
            new_name='first_name_kana',
        ),
        migrations.AddField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='last_name_kana',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]