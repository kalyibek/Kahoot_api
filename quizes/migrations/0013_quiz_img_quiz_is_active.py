# Generated by Django 4.0.6 on 2022-07-26 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0012_remove_questionresult_quiz_result_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='img',
            field=models.ImageField(null=True, upload_to='C:\\Users\\Kalyibek\\PycharmProjects\\Zeon_1st_week\\Kahoot\\media\\images'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
