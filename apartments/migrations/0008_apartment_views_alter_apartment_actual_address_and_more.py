# Generated by Django 4.2.11 on 2024-05-22 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0007_apartment_actual_address_apartment_maps_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='views',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='actual_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='district',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='maps_link',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
