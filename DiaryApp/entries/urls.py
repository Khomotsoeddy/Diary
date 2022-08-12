from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='host'),
    path('add/',views.add, name='add')
]