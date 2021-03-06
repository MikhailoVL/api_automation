# Generated by Django 3.1.7 on 2021-03-01 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20210228_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='price',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(blank=True, default='2021-03-01'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(blank=True, default='2021-03-01'),
        ),
        migrations.AlterField(
            model_name='score',
            name='date_create',
            field=models.DateField(blank=True, default='2021-03-01'),
        ),
    ]
