from django.contrib import admin  # Добавьте этот импорт
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the homepage!")

urlpatterns = [
    path('admin/', admin.site.urls),  # Теперь должно работать
    path('api/', include('products.urls')),  # Пример для API
    path('', home),  # Главная страница
]
