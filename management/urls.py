from django.urls import path
from . import views

urlpatterns = [path('', views.start),
               path('home/', views.strategies_page),
               path('rests', views.get_rest),]