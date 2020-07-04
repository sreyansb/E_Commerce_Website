# Generated by Django 3.0.7 on 2020-06-29 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_orders_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('update_desc', models.CharField(max_length=5000)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Orders')),
            ],
        ),
    ]
