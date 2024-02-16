# Generated by Django 4.2.9 on 2024-02-14 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0003_alter_basket_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='price',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='basket',
            name='shopper',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
