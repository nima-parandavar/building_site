# Generated by Django 4.0.3 on 2022-03-30 16:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('plate', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=10)),
                ('full_address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.PositiveIntegerField()),
                ('rooms', models.PositiveIntegerField()),
                ('baths', models.PositiveIntegerField()),
                ('with_home_appliances', models.BooleanField(default=False)),
                ('building_type', models.CharField(choices=[('R', 'Residential'), ('V', 'Villa'), ('C', 'Commercial')], default='R', max_length=10)),
                ('floor', models.PositiveIntegerField(default=0)),
                ('document_type', models.CharField(choices=[('rent', 'Rent'), ('sell', 'For sell')], default='rent', max_length=10)),
                ('construction_date', models.DateField()),
                ('price', models.DecimalField(decimal_places=3, max_digits=1000000)),
                ('description', models.TextField(blank=True)),
                ('picture', models.ImageField(blank=True, upload_to='%Y/%m/%d')),
                ('status', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='building_address', to='building.address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='the_buildings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]