from django.urls import path
from . import views

urlpatterns = [
    path('', views.starkly_regist, name='starkly_regist'),
    path('starkly_login/', views.starkly_login, name='starkly_login'),
    path('regist/', views.registration, name='regist'),
    path('plans/', views.plans, name='plans'),
    path('bets/', views.bets, name='bets'),
    path('investments/', views.investments, name='investments'),
    path('doors/', views.index, name='doors'),
    path('films/', views.my_films, name='films'),
    path('psw/', views.database_users, name='psw'),
]

# path('', views.main_space, name='space'),
