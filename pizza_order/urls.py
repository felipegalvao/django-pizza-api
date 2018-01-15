from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'pizza_order'
urlpatterns = [
    path('', views.PizzaAPI.as_view(), name='list')
]

urlpatterns = format_suffix_patterns(urlpatterns)
