# Generated by Django 4.0.6 on 2022-07-25 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0009_questionresult_group_quizresult_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='groups',
        ),
    ]
