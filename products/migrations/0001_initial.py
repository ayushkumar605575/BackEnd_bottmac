# Generated by Django 5.0.2 on 2024-03-05 16:56

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('productId', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('productName', models.CharField(max_length=100)),
                ('productImage', django.contrib.postgres.fields.ArrayField(base_field=models.BinaryField(), default=list, size=None)),
                ('productFeatures', models.TextField(max_length=500)),
            ],
        ),
    ]