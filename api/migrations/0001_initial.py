# Generated by Django 2.2.11 on 2020-03-05 03:37

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('address1', models.CharField(max_length=100, verbose_name='Address 1')),
                ('address2', models.CharField(max_length=100, verbose_name='Address 2')),
                ('zip_code', models.CharField(max_length=12, verbose_name='Zip code')),
                ('city', models.CharField(max_length=100, verbose_name='City name')),
                ('country', models.CharField(max_length=100, verbose_name='Country name')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='RealState',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80, verbose_name='Name')),
                ('price', models.BigIntegerField(verbose_name='Price in cents')),
                ('description', models.TextField(verbose_name='Description')),
                ('approved', models.BooleanField(default=False, verbose_name='Approval state')),
                ('latitude', models.CharField(max_length=50, verbose_name='Latitude')),
                ('longitude', models.CharField(max_length=50, verbose_name='Longitude')),
                ('files', jsonfield.fields.JSONField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.Address')),
            ],
        ),
    ]