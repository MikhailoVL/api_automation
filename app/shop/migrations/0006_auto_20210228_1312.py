# Generated by Django 3.1.7 on 2021-02-28 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20210227_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_payment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(blank=True, default='2021-02-28'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(blank=True, default='2021-02-28'),
        ),
        migrations.AlterField(
            model_name='score',
            name='date_create',
            field=models.DateField(blank=True, default='2021-02-28'),
        ),
    ]