# Generated by Django 4.2.11 on 2024-05-07 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0006_alter_favorite_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='actual_address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='apartment',
            name='maps_link',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='bath_rooms',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='beds',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apartments.city'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='district',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='rooms',
            field=models.IntegerField(null=True),
        ),
    ]
