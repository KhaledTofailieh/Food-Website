from django.urls import path
from . import views

urlpatterns = [
    path('', views.start),
    path('index', views.show_index),
    path('login', views.login),
    path('home', views.get_rests_list),
    path('home/<id>', views.get_rest_dishes),
    path('home/<id_1>/<id_2>', views.get_related_dishes_2),
    path('dishes', views.get_first_list_page),
    path('dishes/<dish_id>', views.get_related_dishes),

]
