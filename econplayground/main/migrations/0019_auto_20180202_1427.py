# Generated by Django 2.0.2 on 2018-02-02 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20180201_1057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='graph',
            name='cobb_douglas_plot_on_k',
        ),
        migrations.AddField(
            model_name='graph',
            name='cobb_douglas_y_name',
            field=models.TextField(default='Y'),
        ),
    ]