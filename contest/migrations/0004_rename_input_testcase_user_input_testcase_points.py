# Generated by Django 4.2.7 on 2023-11-20 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0003_alter_contest_player1_alter_contest_player2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testcase',
            old_name='input',
            new_name='user_input',
        ),
        migrations.AddField(
            model_name='testcase',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]