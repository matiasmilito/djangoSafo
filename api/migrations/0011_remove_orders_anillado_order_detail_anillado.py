# Generated by Django 4.1.1 on 2022-11-04 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_orders_anillado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='anillado',
        ),
        migrations.AddField(
            model_name='order_detail',
            name='anillado',
            field=models.BooleanField(default=False),
        ),
    ]
