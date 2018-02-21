# Generated by Django 2.0.2 on 2018-02-06 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_graph_alpha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graph',
            name='correct_feedback',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='graph',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='graph',
            name='incorrect_feedback',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='graph',
            name='instructor_notes',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='graph',
            name='intersection_horiz_line_label',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='graph',
            name='intersection_label',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='graph',
            name='intersection_vert_line_label',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='graph',
            name='line_1_feedback_decrease',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='graph',
            name='line_1_feedback_increase',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='graph',
            name='line_1_label',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='graph',
            name='line_2_feedback_decrease',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='graph',
            name='line_2_feedback_increase',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='graph',
            name='line_2_label',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='graph',
            name='x_axis_label',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='graph',
            name='y_axis_label',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]