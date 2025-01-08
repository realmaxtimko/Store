from django.contrib import admin
from .models import GirlsClothing

@admin.register(GirlsClothing)
class GirlsClothingAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock')
    list_filter = ('category', 'size', 'color')
    search_fields = ('name', 'category')
    prepopulated_fields = {'slug': ('name',)}