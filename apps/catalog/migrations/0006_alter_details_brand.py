# Generated by Django 4.2.9 on 2024-02-14 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_details_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='brand',
            field=models.CharField(max_length=70),
        ),
    ]