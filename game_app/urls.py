from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tic-tac-toe/', views.tic_tac_toe, name='tic_tac_toe'),
]