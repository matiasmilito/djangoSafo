# Generated by Django 4.1.1 on 2022-12-14 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_order_detail_anillado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dni',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='legajo',
            field=models.CharField(default=0, max_length=12),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.BigIntegerField(default=0),
        ),
    ]
