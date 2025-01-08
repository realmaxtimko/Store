from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from male.models import MensClothing
from main.utils import ProductDetailViewMixins, ViewMixins
from django.views import View
from django.views.decorators.cache import cache_page


class MensView(ViewMixins, View):
    model = MensClothing
    template = 'MensClothes.html'
    title = 'Одяг для чоловіків'

class ProductDetailViewMens(ProductDetailViewMixins, View):
    model = MensClothing

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context['add_to_cart_url'] = reverse(
            'add_to_cart',
            kwargs={
                'app_label': product._meta.app_label,
                'model_name': product._meta.model_name,
                'object_id': product.id
            }
        )
        return context