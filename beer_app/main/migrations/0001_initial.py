# Generated by Django 4.1.6 on 2023-02-08 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('town', models.CharField(max_length=100)),
                ('postal_code', models.IntegerField(max_length=10)),
            ],
        ),
    ]
