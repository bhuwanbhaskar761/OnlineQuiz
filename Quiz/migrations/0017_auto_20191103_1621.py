# Generated by Django 2.2.6 on 2019-11-03 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0016_auto_20191103_1607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizresult',
            name='your_ans',
        ),
        migrations.CreateModel(
            name='FinalResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_ans', models.CharField(max_length=100, null=True)),
                ('que', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Quiz.Question')),
            ],
        ),
    ]
