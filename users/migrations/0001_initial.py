# Generated by Django 2.2.7 on 2019-11-22 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('dpi', models.IntegerField()),
                ('weight', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=20)),
                ('brand', models.CharField(max_length=30)),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Passenger')),
            ],
        ),
    ]
