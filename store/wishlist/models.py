from django.conf import settings
from django.db import models


class Wishlist(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="wishlist"
    )
    product_mans = models.ForeignKey(
        'male.MensClothing',  # Вказуємо правильне ім'я моделі з додатку store
        on_delete=models.CASCADE, 
        related_name="liked_by_mans", 
        null=True, 
        blank=True
    )
    product_womans = models.ForeignKey(
        'female.WomensClothing',  # Вказуємо правильне ім'я моделі з додатку store
        on_delete=models.CASCADE, 
        related_name="liked_by_womans", 
        null=True, 
        blank=True
    )
    product_boys = models.ForeignKey(
        'boys.BoysClothing',  # Вказуємо правильне ім'я моделі з додатку store
        on_delete=models.CASCADE, 
        related_name="liked_by_boys", 
        null=True, 
        blank=True
    )
    product_girls = models.ForeignKey(
        'girls.GirlsClothing',  # Вказуємо правильне ім'я моделі з додатку store
        on_delete=models.CASCADE, 
        related_name="liked_by_girls", 
        null=True, 
        blank=True
    )
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        products = [
            f"mans: {self.product_mans}" if self.product_mans else "",
            f"womans: {self.product_womans}" if self.product_womans else "",
            f"boys: {self.product_boys}" if self.product_boys else "",
            f"girls: {self.product_girls}" if self.product_girls else "",
        ]
        products = [p for p in products if p]  # Видалити пусті значення
        return f"{self.user.username} likes {'; '.join(products)}"

    class Meta:
        verbose_name = "Вибране"
        verbose_name_plural = "Вибране"
        unique_together = [
            ('user', 'product_mans'),
            ('user', 'product_womans'),
            ('user', 'product_boys'),
            ('user', 'product_girls'),
        ]
