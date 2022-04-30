# Generated by Django 4.0.4 on 2022-04-30 08:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuel',
                 models.CharField(choices=[('CNG', 'CNG'), ('Petrol', 'Petrol'), ('Diesel', 'Diesel')], default='CNG',
                                  max_length=6)),
                ('vehicle_segment',
                 models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], default='A', max_length=1)),
                ('premium', models.PositiveIntegerField()),
                ('bodily_injury_liability', models.BooleanField(default=False)),
                ('personal_injury_protection', models.BooleanField(default=False)),
                ('property_damage_liability', models.BooleanField(default=False)),
                ('collision', models.BooleanField(default=False)),
                ('comprehensive', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerPolicies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_purchase', models.DateField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='policies',
                                               to='customer.customer')),
                ('policy',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_policy',
                                   to='policy.policy')),
            ],
        ),
    ]
