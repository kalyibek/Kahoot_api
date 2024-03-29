# Generated by Django 4.0.6 on 2022-07-25 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_user_groups_delete_customgroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='final_score',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='passed_tests_number',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
