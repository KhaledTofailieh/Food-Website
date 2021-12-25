from django.db import models


class Dish(models.Model):
    rest_id = models.CharField(max_length=30)
    menu_name = models.CharField(max_length=30)
    dish_id = models.CharField(max_length=30)
    menu_id = models.CharField(max_length=30)
    dish_name = models.CharField(max_length=30)
    dish_price = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    rest_name = models.CharField(max_length=50)
    rest_a_name = models.CharField(max_length=50)
    img_url = models.ImageField(upload_to='pic', null=True)

    def __str__(self):
        return self.dish_name + ", " + self.dish_id


class Order(models.Model):
    restaurant_address = models.CharField(max_length=50)
    restaurant_name = models.CharField(max_length=50)
    restaurant_a_name = models.CharField(max_length=50)
    user_id = models.CharField(max_length=40)
    restaurant_id = models.CharField(max_length=30)
    rate = models.CharField(max_length=10)
    order_time = models.CharField(max_length=30)
    bill_total = models.CharField(max_length=20)
    paid = models.CharField(max_length=5)
    order_id = models.CharField(max_length=50)
    dish_id = models.CharField(max_length=50)
    bill_id = models.CharField(max_length=50)
    dish_price = models.CharField(max_length=20)
    quantity = models.CharField(max_length=10)
    order_total = models.CharField(max_length=10)
    user_address_label = models.CharField(max_length=50)
    user_address = models.CharField(max_length=50)

    def __str__(self):
        return self.order_id + ", " + self.user_id


class User(models.Model):
    user_id = models.CharField(max_length=20)
    address = models.CharField(max_length=20)

    def __str__(self):
        return self.user_id + "|" + self.address


class Rest(models.Model):
    name = models.CharField(max_length=30)
    name_a = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    rest_id = models.CharField(max_length=10)
    img = models.ImageField(upload_to='rests_pic', null=True)

    def __str__(self):
        return self.name_a
