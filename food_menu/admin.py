from django.contrib import admin
from .models import Dish, Order,  Rest, User

# Register your models here.

admin.site.register(Dish)
admin.site.register(Order)
admin.site.register(User)
admin.site.register(Rest)
