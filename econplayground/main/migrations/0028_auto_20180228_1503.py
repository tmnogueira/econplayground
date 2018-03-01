# Generated by Django 2.0.2 on 2018-02-28 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_auto_20180228_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graph',
            name='line_1_decrease_score',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='graph',
            name='line_1_increase_score',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='graph',
            name='line_2_decrease_score',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='graph',
            name='line_2_increase_score',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='submission',
            name='score',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=8),
        ),
    ]
