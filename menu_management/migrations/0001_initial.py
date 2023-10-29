# Generated by Django 4.2 on 2023-09-30 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cautions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='タイトル')),
                ('content', models.TextField(blank=True, null=True, verbose_name='内容')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
            ],
            options={
                'db_table': 'cautions',
            },
        ),
        migrations.CreateModel(
            name='Menus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='メニュー名')),
                ('description', models.TextField(blank=True, null=True, verbose_name='説明')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='価格')),
                ('duration', models.IntegerField(blank=True, null=True, verbose_name='所要時間')),
                ('is_option', models.BooleanField(blank=True, null=True, verbose_name='オプション')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
            ],
            options={
                'db_table': 'menus',
            },
        ),
    ]