# Generated by Django 4.0.4 on 2022-06-02 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_alter_watchlist_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watchlist',
            old_name='watchList',
            new_name='watchlist',
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='user',
            field=models.CharField(default='abhi', max_length=200),
        ),
    ]
