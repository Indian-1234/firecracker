# Generated by Django 4.2.3 on 2023-07-24 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fireapp', '0012_remove_delivered_ordered_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivered',
            name='delivery_date',
            field=models.DateField(default='2020-12-12'),
            preserve_default=False,
        ),
    ]
