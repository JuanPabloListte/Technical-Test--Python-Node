from django.contrib import admin
from django.urls import include, path
from api.views import Hola

urlpatterns = [
    path('', Hola.as_view()),
]
