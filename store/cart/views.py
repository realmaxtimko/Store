from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import Cart

def add_to_cart(request, app_label, model_name, object_id):
    if not request.user.is_authenticated:
        return redirect('loginView')

    try:
        # Отримання ContentType
        content_type = ContentType.objects.get(app_label=app_label, model=model_name)
        # Перевірка існування об'єкта
        model_class = content_type.model_class()
    except ContentType.DoesNotExist:
        return HttpResponseBadRequest("Категорія не знайдена.")
    except model_class.DoesNotExist:
        return HttpResponseBadRequest("Товар не знайдено.")

    # Додавання або оновлення запису в кошику
    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        content_type=content_type,
        object_id=object_id,
        defaults={'quantity': 1},
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('main_view')

def cartView(request):
    # Перевірка, чи користувач автентифікований
    if not request.user.is_authenticated:
        return redirect('loginView')  # Перенаправлення на сторінку входу

    # Отримання кошика користувача
    try:
        cart = Cart.objects.filter(user=request.user)
    except Cart.DoesNotExist:
        cart = None

    # Передача даних у шаблон
    context = {
        'cart': cart
    }
    return render(request, 'cart.html', context)

def RemoveFromCart(request, app_label, model_name, object_id):
    if not request.user.is_authenticated:
        return redirect('loginView')
    
    content_type = ContentType.objects.get(app_label=app_label, model=model_name)
    # Додавання або оновлення запису в кошику
    cart_item = Cart.objects.get(
                user=request.user,
                content_type=content_type,
                object_id=object_id,
            )
    cart_item.delete()
    return redirect('cart')