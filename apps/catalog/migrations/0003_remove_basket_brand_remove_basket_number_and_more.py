# Generated by Django 4.2.9 on 2024-02-27 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_basket_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='basket',
            name='number',
        ),
        migrations.AlterField(
            model_name='basket',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('O', 'Ordered')], default='P', max_length=1),
        ),
    ]