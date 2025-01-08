from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class WomensClothing(models.Model):
    # Основна інформація про товар
    name = models.CharField(max_length=255, verbose_name="Назва")
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    description = models.TextField(verbose_name="Опис", blank=True, null=True)
    category = models.CharField(
        max_length=100,
        choices=[
            ('shirts', 'Сорочки'),
            ('tshirts', 'Футболки'),
            ('jeans', 'Джинси'),
            ('jackets', 'Куртки'),
            ('coats', 'Пальта'),
            ('down_jackets', 'Пуховики'),
            ('dresses', 'Сукні'),
            ('blazers', 'Піджаки'),
            ('vests', 'Жилети'),
            ('blouses', 'Блузки'),
            ('skirts', 'Спідниці'),
            ('shorts', 'Шорти'),
            ('sweatshirts', 'Світшоти'),
            ('tops', 'Топи'),
            ('shoes', 'Взуття'),
            ('accessories', 'Аксесуари'),
        ],
        verbose_name="Категорія"
    )

    # Розміри, доступність і ціни
    size = models.CharField(
        max_length=10,
        choices=[
            ('XS', 'XS'),
            ('S', 'S'),
            ('M', 'M'),
            ('L', 'L'),
            ('XL', 'XL'),
            ('XXL', 'XXL'),
        ],
        verbose_name="Розмір"
    )
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Ціна")
    discount_price = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True, verbose_name="Ціна зі знижкою"
    )
    in_stock = models.BooleanField(default=True, verbose_name="В наявності")

    # Зображення товару
    image = models.ImageField(upload_to='Womens_clothing/', verbose_name="Зображення", blank=True, null=True)

    # Додаткова інформація
    material = models.CharField(max_length=100, verbose_name="Матеріал", blank=True, null=True)
    brand = models.CharField(max_length=100, verbose_name="Бренд", blank=True, null=True)
    color = models.CharField(max_length=50, verbose_name="Колір", blank=True, null=True)

    # Дата створення та оновлення
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата додавання")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата оновлення")

    def save(self, *args, **kwargs):
        # Автоматично генеруємо slug на основі заголовка, якщо його немає
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = "Жіночий одяг"
        verbose_name_plural = "Жіночий одяг"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.category}"

    @property
    def is_discounted(self):
        """Перевірка, чи є знижка на товар"""
        return self.discount_price is not None and self.discount_price < self.price

    def get_discount_percentage(self):
        """Розрахунок відсотку знижки"""
        if self.is_discounted:
            return round((1 - self.discount_price / self.price) * 100, 2)
        return 0
