from django.urls import path
from quotes.views import quote_view


urlpatterns = [
    path('', quote_view, name='quote_page'),
]