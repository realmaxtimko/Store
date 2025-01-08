from django.contrib import admin
from .models import WomensClothing

@admin.register(WomensClothing)
class WomensClothingAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'discount_price', 'in_stock', 'created_at')
    list_filter = ('category', 'size', 'brand', 'in_stock')
    search_fields = ('name', 'brand', 'description')
    prepopulated_fields = {'slug': ('name',)}
