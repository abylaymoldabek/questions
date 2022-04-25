# Generated by Django 4.0.4 on 2022-04-25 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_useranswer_remove_answer_choice_remove_answer_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='useranswer',
            name='positive_percentage',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.question'),
        ),
        migrations.AlterUniqueTogether(
            name='useranswer',
            unique_together={('phone', 'created_date')},
        ),
    ]