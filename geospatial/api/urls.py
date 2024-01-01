from django.urls import path
from .views import getGeoData


urlpatterns = [
    path('geodata/', getGeoData.as_view(), name='getGeoData'),
]
