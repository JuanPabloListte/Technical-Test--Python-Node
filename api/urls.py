from django.contrib import admin
from django.urls import include, path
from api.views import CargarPDFView

urlpatterns = [
    path('', CargarPDFView.as_view(), name='cargar_pdf'),
]
