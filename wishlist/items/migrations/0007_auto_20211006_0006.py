# Generated by Django 3.2.7 on 2021-10-06 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_auto_20211005_2329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemlist',
            name='user_list',
        ),
        migrations.AddField(
            model_name='itemlist',
            name='user_list',
            field=models.ManyToManyField(to='items.Item'),
        ),
    ]
