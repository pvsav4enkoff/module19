# Generated by Django 5.1.3 on 2024-11-30 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0002_remove_game_buyer_game_buyer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='description',
            field=models.TextField(),
        ),
    ]