# Generated by Django 2.0.6 on 2018-06-20 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0042_auto_20180601_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='graph',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Graph', unique=True),
        ),
    ]
