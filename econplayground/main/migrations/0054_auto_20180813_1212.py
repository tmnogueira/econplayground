# Generated by Django 2.1 on 2018-08-13 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0053_auto_20180710_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedGraph',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('main.graph',),
        ),
        migrations.AddField(
            model_name='submission',
            name='feedback_fulfilled',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='submission',
            name='feedback_unfulfilled',
            field=models.TextField(blank=True, default=''),
        ),
    ]
