from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cart")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # Для вибору категорії
    object_id = models.PositiveIntegerField()  # ID об'єкта
    item = GenericForeignKey('content_type', 'object_id')  # Дозволяє зв'язок із будь-якою моделлю
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def get_price(self):
        # Отримати ціну товару
        return self.item.price * self.quantity

    def get_image(self):
        # Отримати зображення товару
        return self.item.image.url

    class Meta:
        verbose_name = "Кошик"
        verbose_name_plural = "Кошик"

        def __str__(self):
            return f"{self.user.username}'s cart - {self.item} x {self.quantity}"
