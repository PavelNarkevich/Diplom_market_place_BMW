# Generated by Django 4.2.9 on 2024-02-20 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
            name='CarElement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='car_element/')),
            ],
            options={
                'verbose_name': 'car element',
                'verbose_name_plural': 'car element',
            },
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=40)),
                ('engine_code', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=15)),
                ('body_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.bodytype')),
            ],
            options={
                'verbose_name': 'Cars',
                'verbose_name_plural': 'Cars',
            },
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='component/')),
                ('element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='elem', to='catalog.carelement')),
            ],
            options={
                'verbose_name': 'component',
                'verbose_name_plural': 'component',
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
                ('name', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'verbose_name': 'EngineType',
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=25, unique=True)),
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
                ('name', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'verbose_name': 'Transmission',
            },
        ),
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('brand', models.CharField(max_length=70)),
                ('number', models.CharField(max_length=70)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='details/')),
                ('quantity', models.IntegerField()),
                ('description', models.CharField(blank=True, max_length=30, null=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('car', models.ManyToManyField(related_name='car', to='catalog.cars')),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='component', to='catalog.component')),
            ],
            options={
                'verbose_name': 'Details',
                'verbose_name_plural': 'Details',
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='cars',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.country'),
        ),
        migrations.AddField(
            model_name='cars',
            name='engine_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.enginetype'),
        ),
        migrations.AddField(
            model_name='cars',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.series'),
        ),
        migrations.AddField(
            model_name='cars',
            name='transmission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.transmission'),
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('number', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=25)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basket1', to='catalog.details')),
                ('shopper', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Basket',
                'verbose_name_plural': 'Basket',
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
