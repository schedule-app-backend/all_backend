# Generated by Django 4.1.13 on 2024-10-14 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=255, unique=True)),
                ('is_teacher', models.BooleanField()),
            ],
            options={
                'db_table': 'clients',
            },
        ),
        migrations.CreateModel(
            name='schedules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule_date', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='schedule_api.clients')),
            ],
            options={
                'db_table': 'schedules',
                'unique_together': {('client', 'schedule_date')},
            },
        ),
        migrations.CreateModel(
            name='classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_bells', models.CharField(blank=True, max_length=50, null=True)),
                ('class_number', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('class_type', models.CharField(blank=True, max_length=50, null=True)),
                ('partner', models.CharField(blank=True, max_length=255, null=True)),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='schedule_api.schedules')),
            ],
            options={
                'db_table': 'classes',
                'unique_together': {('schedule', 'class_number')},
            },
        ),
    ]