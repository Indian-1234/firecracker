# Generated by Django 4.2.3 on 2023-07-14 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fireapp', '0002_orders_quantitity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='product_name',
            field=models.CharField(max_length=255),
        ),
    ]
