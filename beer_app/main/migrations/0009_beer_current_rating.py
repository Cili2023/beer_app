# Generated by Django 4.1.6 on 2023-03-14 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_review_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='current_rating',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
        ),
    ]
