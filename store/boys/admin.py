from django.contrib import admin
from .models import BoysClothing

@admin.register(BoysClothing)
class BoysClothingAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock')
    list_filter = ('category', 'size', 'color')
    search_fields = ('name', 'category')
    prepopulated_fields = {'slug': ('name',)}