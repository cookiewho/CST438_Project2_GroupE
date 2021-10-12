# Generated by Django 3.2.8 on 2021-10-10 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('image', models.URLField(default='None')),
                ('category', models.CharField(default='None', max_length=100)),
                ('description', models.TextField(default='None')),
            ],
        ),
        migrations.CreateModel(
            name='itemList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.ManyToManyField(to='items.Item')),
                ('list_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.list')),
            ],
        ),
    ]
