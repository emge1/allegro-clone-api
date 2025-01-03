# Generated by Django 4.0.2 on 2022-03-07 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0002_rename_added_by_merchant_product_added_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductTransaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_count', models.IntegerField(default=1)),
                ('description', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
