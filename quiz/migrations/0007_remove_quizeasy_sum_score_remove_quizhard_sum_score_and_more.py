# Generated by Django 4.2.4 on 2023-08-26 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_participant_delete_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizeasy',
            name='sum_score',
        ),
        migrations.RemoveField(
            model_name='quizhard',
            name='sum_score',
        ),
        migrations.RemoveField(
            model_name='quiznormal',
            name='sum_score',
        ),
        migrations.AddField(
            model_name='quizeasy',
            name='plus_score',
            field=models.IntegerField(default=5, verbose_name='플러스 점수'),
        ),
        migrations.AddField(
            model_name='quizhard',
            name='plus_score',
            field=models.IntegerField(default=15, verbose_name='플러스 점수'),
        ),
        migrations.AddField(
            model_name='quiznormal',
            name='plus_score',
            field=models.IntegerField(default=10, verbose_name='플러스 점수'),
        ),
    ]
