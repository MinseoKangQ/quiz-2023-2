# Generated by Django 4.2.4 on 2023-08-26 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_remove_quizeasy_sum_score_remove_quizhard_sum_score_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizhard',
            name='answer10_3',
            field=models.CharField(default='인성관 405호', max_length=10, verbose_name='10번_3 정답'),
        ),
    ]