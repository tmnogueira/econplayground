# Generated by Django 2.2.4 on 2019-08-27 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0062_auto_20190719_1553'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ('cohort', 'order')},
        ),
        migrations.AlterField(
            model_name='graph',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.Topic'),
        ),
    ]