# Generated by Django 4.2.9 on 2024-02-15 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_details_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]