
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('weather.urls')), #отслеживание нового адреса через приложение weather с файла urls

]
