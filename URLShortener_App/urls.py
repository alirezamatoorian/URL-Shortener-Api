from django.urls import path
from . import views


app_name = 'URLShortener_App'


urlpatterns = [
    path("URLShortener/",views.URLShortenerView.as_view(),name='URLShortener'),
]