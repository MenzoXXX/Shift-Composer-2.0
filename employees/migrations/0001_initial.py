# Generated by Django 4.2.4 on 2023-10-15 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pracownik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=50)),
                ('nazwisko', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Dostepnosc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dzien', models.DateField()),
                ('dostepnosc', models.CharField(max_length=20)),
                ('godziny_dostepnosci', models.CharField(blank=True, max_length=100, null=True)),
                ('pracownik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.pracownik')),
            ],
        ),
    ]
