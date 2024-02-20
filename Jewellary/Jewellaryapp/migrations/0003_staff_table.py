# Generated by Django 5.0.1 on 2024-02-11 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jewellaryapp', '0002_productsinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='staff_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('confirm_password', models.CharField(max_length=30)),
                ('approval', models.BooleanField(default=False)),
            ],
        ),
    ]