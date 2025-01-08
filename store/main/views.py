from django.shortcuts import render
from .forms import SearchForm
from male.models import MensClothing
from female.models import WomensClothing
from boys.models import BoysClothing
from girls.models import GirlsClothing
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
from rest_framework.response import Response
from female.models import WomensClothing
from .serializers import WomanClothingSerializer
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from django.db.models import Q


def main_view(request):
    return render(request, 'base.html')

def reference_view(request):
    return render(request, 'reference.html')

def search_view(request):
    form = SearchForm(request.GET)
    results = []
    query = None

    if form.is_valid():
        query = form.cleaned_data.get('query')
        if query:
            # Виконуємо пошук у різних моделях
            results_mens = MensClothing.objects.filter(Q(name__icontains=query))
            results_womens = WomensClothing.objects.filter(Q(name__icontains=query))
            results_boys = BoysClothing.objects.filter(Q(name__icontains=query))
            results_girls = GirlsClothing.objects.filter(Q(name__icontains=query))
            # Об'єднуємо результати в один список
            results = list(results_mens) + list(results_womens) + list(results_boys) + list(results_girls)

    return render(request, 'search.html', {
        'form': form,
        'query': query,
        'results': results,
    })

def user_view(request):
    username = request.GET.get('username')  # Отримуємо ім'я користувача з параметра запиту
    try:
        user = User.objects.get(username=username)  # Пошук користувача за username
        print(user)
    except User.DoesNotExist:
        user = None  # Якщо користувача не знайдено
    return render(request, 'base.html', {'user': user})

class ObjectAPIView(APIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        # Метод повертає queryset для моделі WomensClothing
        return WomensClothing.objects.all()

    def get(self, request):
        # Використовуємо self.get_queryset() для отримання даних
        queryset = self.get_queryset()
        serializer = WomanClothingSerializer(queryset, many=True)
        return Response(serializer.data)