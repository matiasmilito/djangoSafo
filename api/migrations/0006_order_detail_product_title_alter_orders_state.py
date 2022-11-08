# Generated by Django 4.1.1 on 2022-10-13 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_orders_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_detail',
            name='product_title',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orders',
            name='state',
            field=models.BooleanField(default=False),
        ),
    ]
