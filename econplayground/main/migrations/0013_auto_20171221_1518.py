# Generated by Django 2.0 on 2017-12-21 20:18

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20171218_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='graph',
            name='cobb_douglas_a',
            field=models.DecimalField(decimal_places=4, default=Decimal('2'), help_text='A = Total factor productivity', max_digits=12),
        ),
        migrations.AddField(
            model_name='graph',
            name='cobb_douglas_alpha',
            field=models.DecimalField(decimal_places=4, default=Decimal('0.65'), help_text='α = output elasticity of capital', max_digits=12),
        ),
        migrations.AddField(
            model_name='graph',
            name='cobb_douglas_k',
            field=models.DecimalField(decimal_places=4, default=Decimal('1'), help_text='K = Capital input', max_digits=12),
        ),
        migrations.AddField(
            model_name='graph',
            name='cobb_douglas_l',
            field=models.DecimalField(decimal_places=4, default=Decimal('0'), help_text='L = Labor input', max_digits=12),
        ),
        migrations.AlterField(
            model_name='graph',
            name='line_1_offset',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='graph',
            name='line_1_slope',
            field=models.DecimalField(decimal_places=4, max_digits=12),
        ),
        migrations.AlterField(
            model_name='graph',
            name='line_2_offset',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='graph',
            name='line_2_slope',
            field=models.DecimalField(decimal_places=4, max_digits=12),
        ),
    ]