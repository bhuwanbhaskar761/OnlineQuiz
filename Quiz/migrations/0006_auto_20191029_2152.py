# Generated by Django 2.2.6 on 2019-10-29 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0005_remove_userdetail_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='news',
            new_name='topic',
        ),
    ]