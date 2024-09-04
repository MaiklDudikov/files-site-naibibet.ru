from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm
# from django.contrib.auth import authenticate, login as auth_login
# from django.contrib import messages


def starkly_regist(request):
    error = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('bets')

    form = UserForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/starkly_regist.html', data)


# def main_space(request):
#     return render(request, 'main/main_space.html')


def starkly_login(request):
    if request.method == 'POST':
        # Перенаправляем на страницу 'bets' без проверки данных
        return redirect('bets')

    return render(request, 'main/starkly_login.html')


def registration(request):
    return render(request, 'main/regist.html')


def plans(request):
    return render(request, 'main/plans.html')


def bets(request):
    return render(request, 'main/bets.html')


def investments(request):
    return render(request, 'main/invest.html')


def database_users(request):
    users_psw = User.objects.all()
    return render(request, 'main/database_users.html', {'user': users_psw})


def my_films(request):
    return render(request, 'main/my_films.html')


# name = request.POST.get("username", "none")
# email = request.POST.get("email")
# password = request.POST.get("password")
# User.objects.create(
#    name=name,
#    email=email,
#    password=password
# )
# render(request, 'main/regist.html', context={"test": name})


def about(request):
    return render(request, 'main/about.html')


def index(request):
    return render(request, 'main/index.html')


# def starkly_login(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         password = request.POST.get('password')

#         # Аутентификация пользователя по никнейму (имени) и паролю
#         user = authenticate(request, username=name, password=password)

#         if user is not None:
#             # Если пользователь существует, выполняем вход
#             auth_login(request, user)
#             return redirect('bets')  # Перенаправляем на страницу 'bets'
#         else:
#             # Если пользователь не найден, выводим сообщение об ошибке
#             messages.error(request, "Такого пользователя не существует")

#     return render(request, 'main/starkly_login.html')
