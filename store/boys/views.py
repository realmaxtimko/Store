from .models import BoysClothing
from main.utils import ProductDetailViewMixins, ViewMixins
from django.views import View
from django.views.decorators.cache import cache_page


class BoysView(ViewMixins, View):
    model = BoysClothing
    template = 'BoysClothes.html'
    title = 'Одяг для хлопчиків'

class ProductDetailViewBoys(ProductDetailViewMixins, View):
    model = BoysClothing