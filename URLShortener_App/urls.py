from django.urls import path
from . import views


app_name = 'URLShortener_App'


urlpatterns = [
    path("urls/",views.URLShortenerView.as_view(),name='urlshortener'),
    path("urls/<str:short_code>/",views.URLRedirectView.as_view(),name='urlredirect'),
    path("urls/<str:short_code>/click-count/",views.ClickCountView.as_view(),name='clickcount'),
]