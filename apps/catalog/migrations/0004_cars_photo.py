# Generated by Django 4.2.9 on 2024-03-01 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_remove_basket_brand_remove_basket_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='car_photo/'),
        ),
    ]
