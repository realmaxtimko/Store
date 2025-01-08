from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.core.cache import cache


def authView(request):
    if request.user.is_authenticated:
        return redirect('main_view')
    else:
        if request.method == "POST":
            form = UserCreationForm(request.POST or None)
            if form.is_valid():
                form.save()
                return redirect('loginView')
        else:
            form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

def loginView(request):
    if request.user.is_authenticated:
        return redirect('main_view')
    else:
        form = AuthenticationForm(data=request.POST or None)  # Використовуйте AuthenticationForm для логіну
        if request.method == 'POST':  # Перевірка на метод POST
            if form.is_valid():  # Перевірка, чи форма валідна
                user = form.get_user()
                login(request, user)  # Виконуємо вхід користувача

                request.session['user_id'] = user.id
                request.session['username'] = user.username
                request.session['is_admin'] = user.is_staff

                return redirect('main_view')  # Перенаправлення після успішного входу
        return render(request, 'login.html', {'form': form})  # Повернення форми для заповнення

def logoutView(request):
    logout(request)
    return redirect('main_view')