# Generated by Django 2.2.6 on 2019-11-03 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0014_auto_20191103_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizresult',
            name='topic',
        ),
    ]
