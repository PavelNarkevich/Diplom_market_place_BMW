# Generated by Django 4.2.9 on 2024-02-06 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BodyType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Body Type',
                'verbose_name_plural': 'Body Type',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, unique=True)),
            ],
            options={
                'verbose_name': 'Country',
            },
        ),
        migrations.CreateModel(
            name='EngineType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'verbose_name': 'Engine Type',
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(max_length=10, unique=True)),
            ],
            options={
                'verbose_name': 'Series',
                'verbose_name_plural': 'Series',
            },
        ),
        migrations.CreateModel(
            name='Transmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'verbose_name': 'Transmission',
            },
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=40)),
                ('engine_code', models.CharField(max_length=20)),
                ('body_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog_cars.bodytype')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog_cars.country')),
                ('engine_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog_cars.enginetype')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog_cars.series')),
                ('transmission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog_cars.transmission')),
            ],
        ),
    ]
