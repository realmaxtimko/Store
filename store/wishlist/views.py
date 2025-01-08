from django.shortcuts import redirect, render
from django.contrib.contenttypes.models import ContentType
from .models import Wishlist


def add_to_wishlist(request, app_label, model_name):
    if not request.user.is_authenticated:
        return redirect('loginView')
        # Отримання ContentType
    content_type = ContentType.objects.get(app_label=app_label, model=model_name)
    

    # Додавання або оновлення запису в кошику
    wishlist_item, created = Wishlist.objects.get_or_create(
        user=request.user,
        content_type=content_type,
)

    if not created:
        wishlist_item.quantity += 1
        wishlist_item.save()

    return redirect('main_view')

def cartView(request):
    # Перевірка, чи користувач автентифікований
    if not request.user.is_authenticated:
        return redirect('loginView')  # Перенаправлення на сторінку входу

    # Отримання кошика користувача
    try:
        wishlist = Wishlist.objects.filter(user=request.user)
    except Wishlist.DoesNotExist:
        wishlist = None

    # Передача даних у шаблон
    context = {
        'wishlist': wishlist
    }
    return render(request, 'wishlist.html', context)