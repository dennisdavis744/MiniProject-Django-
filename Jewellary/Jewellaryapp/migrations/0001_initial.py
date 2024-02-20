# Generated by Django 5.0.1 on 2024-02-08 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer_registeration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('confirm_password', models.CharField(max_length=30)),
            ],
        ),
    ]
