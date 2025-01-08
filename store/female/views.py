from django.shortcuts import render
from .models import WomensClothing
from main.utils import ProductDetailViewMixins, ViewMixins
from django.views import View
from django.views.decorators.cache import cache_page


class WomansView(ViewMixins, View):
    model = WomensClothing
    template = 'WomansClothes.html'
    title = 'Одяг для жінок'
    
class ProductDetailViewWomans(ProductDetailViewMixins, View):
    model = WomensClothing
    