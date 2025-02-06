from django.urls import path
from . import views

urlpatterns = [
    path('appurl/', views.home, name='home'),
]