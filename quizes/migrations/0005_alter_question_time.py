# Generated by Django 4.0.6 on 2022-07-21 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0004_remove_quiz_time_question_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='time',
            field=models.IntegerField(default=25),
        ),
    ]