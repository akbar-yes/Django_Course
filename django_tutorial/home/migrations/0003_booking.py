# Generated by Django 4.0.3 on 2022-04-17 20:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_doctors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=255)),
                ('p_phone', models.CharField(max_length=255)),
                ('p_email', models.EmailField(max_length=254)),
                ('booking_date', models.DateField(default=datetime.datetime.now)),
                ('dep_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.departments')),
                ('doc_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.doctors')),
            ],
        ),
    ]
