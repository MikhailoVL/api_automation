# Generated by Django 3.1.7 on 2021-03-01 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20210301_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.order'),
        ),
    ]
