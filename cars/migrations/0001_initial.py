# Generated by Django 4.2 on 2024-12-27 18:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('mileage_type', models.CharField(choices=[('KM', 'km'), ('MIL', 'mil')], max_length=5)),
                ('currency_type', models.CharField(choices=[('USD', 'USD'), ('EUR', 'EUR'), ('AZN', 'AZN')], max_length=5)),
                ('owner_type', models.CharField(choices=[('FIRST', 'Birinci'), ('SECOND', 'İkinci'), ('THIRD', 'Üçüncü'), ('OTHER', 'Dördüncü və ya daha çox')], max_length=10)),
                ('transmission_type', models.CharField(choices=[('FRONT', 'Ön'), ('REAR', 'Arxa'), ('FULL', 'Tam')], max_length=10)),
                ('seat_count', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8+', '8+')], max_length=3)),
                ('is_crashed', models.BooleanField(default=False)),
                ('is_damaged', models.BooleanField(default=False)),
                ('is_colored', models.BooleanField(default=False)),
                ('with_credit', models.BooleanField(default=False)),
                ('barter', models.BooleanField(default=False)),
                ('mileage', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000)])),
                ('price', models.DecimalField(decimal_places=0, max_digits=8)),
                ('released_date', models.DateField(auto_now_add=True)),
                ('engine_power', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10000)])),
                ('vin_code', models.CharField(max_length=17, validators=[django.core.validators.MinLengthValidator(17)])),
                ('info', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CarSupply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EngineCapacity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ForCountry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FuelType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='GearBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RoofType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_models', to='cars.brand')),
            ],
        ),
        migrations.CreateModel(
            name='AnnouncementImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='announcements')),
                ('announcement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.announcement')),
            ],
        ),
        migrations.AddField(
            model_name='announcement',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announcements', to='cars.brand'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='car_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announcements', to='cars.carmodel'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='car_supply',
            field=models.ManyToManyField(related_name='announcement', to='cars.carsupply'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announcements', to='cars.color'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='engine_capacity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announcements', to='cars.enginecapacity'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='for_country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announcements', to='cars.forcountry'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='fuel_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announcements', to='cars.fueltype'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='gear_box',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announcements', to='cars.gearbox'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='roof_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announcements', to='cars.rooftype'),
        ),
    ]