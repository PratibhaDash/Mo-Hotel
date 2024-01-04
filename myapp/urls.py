from django.urls import path
from .views import login, welcome, menu, logout

urlpatterns = [
    path('', login, name='login'),
    path('welcome/', welcome, name='welcome'),
    path('menu/', menu, name='menu'),
    path('logout/', logout, name='logout'),
]