# Generated by Django 3.1.7 on 2021-02-25 18:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(blank=True, default=False)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.PositiveIntegerField(default=0)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_create', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.product'),
        ),
    ]
