# Generated by Django 3.1 on 2020-08-22 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_auto_20200809_1616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='card_number',
        ),
        migrations.AddField(
            model_name='user',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
    ]