from .models import GirlsClothing
from main.utils import ProductDetailViewMixins, ViewMixins
from django.views import View
from django.views.decorators.cache import cache_page


class GirlsView(ViewMixins, View):
    model = GirlsClothing
    template = 'GirlsClothes.html'
    title = 'Одяг для дівчат'

class ProductDetailViewGirls(ProductDetailViewMixins, View):
    model = GirlsClothing