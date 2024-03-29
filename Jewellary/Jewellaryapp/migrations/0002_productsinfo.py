# Generated by Django 5.0.1 on 2024-02-08 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jewellaryapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='productsinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('material', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
    ]
