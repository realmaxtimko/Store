from django.db import models
from django.utils.text import slugify


class GirlsClothing(models.Model):
    CATEGORY_CHOICES = [
        ('dress', 'Сукні'),
        ('blouse', 'Блузки'),
        ('skirt', 'Спідниці'),
        ('pants', 'Штани'),
        ('shorts', 'Шорти'),
        ('jacket', 'Куртки'),
        ('sweater', 'Светри'),
        ('shoes', 'Взуття'),
        ('accessories', 'Аксесуари'),
    ]

    name = models.CharField(max_length=100, verbose_name="Назва")
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        verbose_name="Категорія"
    )
    size = models.CharField(max_length=10, verbose_name="Розмір")
    color = models.CharField(max_length=30, verbose_name="Колір")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    stock = models.PositiveIntegerField(verbose_name="Кількість на складі")
    description = models.TextField(blank=True, null=True, verbose_name="Опис")
    image = models.ImageField(upload_to='girls_clothing/', blank=True, null=True, verbose_name="Зображення")

    def save(self, *args, **kwargs):
        # Автоматично генеруємо slug на основі заголовка, якщо його немає
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Одяг для дівчаток"
        verbose_name_plural = "Одяг для дівчаток"

    def __str__(self):
        return f"{self.name} ({self.category}) - {self.price} грн"
