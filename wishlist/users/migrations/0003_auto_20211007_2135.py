# Generated by Django 3.2.7 on 2021-10-08 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20211005_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userlist',
            name='list_id',
        ),
        migrations.RemoveField(
            model_name='userlist',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Update',
        ),
        migrations.DeleteModel(
            name='userList',
        ),
    ]