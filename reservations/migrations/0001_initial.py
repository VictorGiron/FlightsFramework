# Generated by Django 2.2.7 on 2019-11-22 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aircrafts', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('aircraft', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aircrafts.Aircraft')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination', to='reservations.Location')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='origin', to='reservations.Location')),
                ('package', models.ManyToManyField(to='users.Package')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Passenger')),
            ],
        ),
    ]
