# Generated by Django 4.0.6 on 2022-07-27 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_user_rank_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='group_rank_place',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]