# Generated by Django 5.0.4 on 2024-05-08 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_comment_star_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='star_rating',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1),
        ),
    ]
