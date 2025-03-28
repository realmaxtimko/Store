# Generated by Django 5.1.3 on 2024-12-01 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoysClothing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Назва')),
                ('category', models.CharField(choices=[('tshirt', 'Футболки'), ('shirt', 'Сорочки'), ('pants', 'Штани'), ('shorts', 'Шорти'), ('jacket', 'Куртки'), ('sweater', 'Светри'), ('shoes', 'Взуття'), ('accessories', 'Аксесуари')], max_length=20, verbose_name='Категорія')),
                ('size', models.CharField(max_length=10, verbose_name='Розмір')),
                ('color', models.CharField(max_length=30, verbose_name='Колір')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ціна')),
                ('stock', models.PositiveIntegerField(verbose_name='Кількість на складі')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Опис')),
                ('image', models.ImageField(blank=True, null=True, upload_to='boys_clothing/', verbose_name='Зображення')),
            ],
            options={
                'verbose_name': 'Одяг для хлопчиків',
                'verbose_name_plural': 'Одяг для хлопчиків',
            },
        ),
    ]
