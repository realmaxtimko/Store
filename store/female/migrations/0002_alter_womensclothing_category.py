# Generated by Django 5.1.3 on 2024-12-04 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('female', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='womensclothing',
            name='category',
            field=models.CharField(choices=[('shirts', 'Сорочки'), ('tshirts', 'Футболки'), ('jeans', 'Джинси'), ('jackets', 'Куртки'), ('coats', 'Пальта'), ('down_jackets', 'Пуховики'), ('dresses', 'Сукні'), ('blazers', 'Піджаки'), ('vests', 'Жилети'), ('blouses', 'Блузки'), ('skirts', 'Спідниці'), ('shorts', 'Шорти'), ('sweatshirts', 'Світшоти'), ('tops', 'Топи'), ('shoes', 'Взуття'), ('accessories', 'Аксесуари')], max_length=100, verbose_name='Категорія'),
        ),
    ]
