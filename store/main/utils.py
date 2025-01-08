from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

class ViewMixins:
    model = None  # Модель, з якою працює Mixin
    template = None  # Шаблон для відображення
    title = None  # Заголовок сторінки

    def get(self, request):
        obj = self.model.objects.all()
        context = {'title': self.title, 'Model': obj}
        return render(request, self.template, context=context)
    
class ProductDetailViewMixins:
    model = None
    slug_field = 'slug'  # Параметр, що вказує на поле slug

    def get(self, request, slug):
        product = self.model.objects.get(slug = slug)
        context = {
            'product': product,
            'name': self.model.__name__,
            'app_label': product._meta.app_label,  # Назва додатку
            'model_name': product._meta.model_name,  # Назва моделі
            'add_to_cart_url': reverse(
                'add_to_cart',
                kwargs={
                    'app_label': product._meta.app_label,
                    'model_name': product._meta.model_name,
                    'object_id': product.id
                }
            )
        }
        return render(request, 'product_detail.html', context=context)