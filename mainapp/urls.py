from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('artikel/<int:artikelnummer>/', views.instruktion_detail, name='instruktion_detail'),
    path('sök/', views.sök, name='sök'),
]
