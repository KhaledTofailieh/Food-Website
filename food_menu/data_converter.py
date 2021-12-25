import pandas as pd
from .models import Dish, Order, User, Rest
import time

DISHES_PATH = r'C:\Users\Khaled\Desktop\Python\graduation_website\assets\data\data.csv'
ORDERS_PATH = r'C:\Users\Khaled\Desktop\Python\graduation_website\assets\data\full_order_all_columns.csv'
USERS_PATH = r'C:\Users\Khaled\Desktop\Python\graduation_website\assets\data\Features_User_with_cluster.csv'
RESTS_PATH = r'C:\Users\Khaled\Desktop\Python\graduation_website\assets\data\restaurants_final.csv'


def convert_dishes_to_sql(path):
    df = pd.read_csv(path)
    dishes = []
    for i in range(len(df)):
        print(i)
        dishes.append(Dish(
            rest_id=df.loc[i]['rest_id'],
            menu_name=df.loc[i]['menu_name'],
            dish_id=df.loc[i]['dish_id'],
            menu_id=df.loc[i]['menu_id'],
            dish_name=df.loc[i]['dish_name'],
            dish_price=df.loc[i]['dish_price'],
            address=df.loc[i]['adress'],
            rest_name=df.loc[i]['name'],
            rest_a_name=df.loc[i]['a_name']))
    Dish.objects.bulk_create(dishes)
    Dish.save()


def convert_orders_to_sql(path):
    df = pd.read_csv(path)
    orders = []

    def add_to_list(item, array):
        array.append(Order(
            restaurant_address=item['adress'],
            restaurant_name=item['name'],
            restaurant_a_name=item['a_name'],
            user_id=item['user_id'],
            restaurant_id=item['restaurant_id'],
            rate=item['rate'],
            order_time=item['time'],
            bill_total=item['total_x'],
            paid=item['paid'],
            order_id=item['id_y'],
            dish_id=item['dish_id'],
            bill_id=item['bill_id'],
            dish_price=item['price'],
            quantity=item['quantity'],
            order_total=item['total_y'],
            user_address_label=item['label'],
            user_address=item['address_']))

    df.apply(add_to_list, axis=1, array=orders)
    Order.objects.bulk_create(orders)
    Order.save()

    # print(df.name)
    #     array.append()
    # for i in range(len(df)):
    #     print(i)
    # orders.append(Order(
    #     restaurant_address=df.loc[i]['adress'],
    #     restaurant_name=df.loc[i]['name'],
    #     restaurant_a_name=df.loc[i]['a_name'],
    #     user_id=df.loc[i]['user_id'],
    #     restaurant_id=df.loc[i]['restaurant_id'],
    #     rate=df.loc[i]['rate'],
    #     order_time=df.loc[i]['time'],
    #     bill_total=df.loc[i]['total_x'],
    #     paid=df.loc[i]['paid'],
    #     order_id=df.loc[i]['id_y'],
    #     dish_id=df.loc[i]['dish_id'],
    #     bill_id=df.loc[i]['bill_id'],
    #     dish_price=df.loc[i]['price'],
    #     quantity=df.loc[i]['quantity'],
    #     order_total=df.loc[i]['total_y'],
    #     user_address_label=df.loc[i]['label'],
    #     user_address=df.loc[i]['address_']))

    # Order.objects.bulk_create(orders)
    # Order.save()


def convert_user_to_sql(path):
    df = pd.read_csv(path)
    users = []
    for i in range(len(df)):
        print(i)
        users.append(User(
            user_id=df.loc[i]['user_id'],
            address=df.loc[i]['user_label']
        ))
    User.objects.bulk_create(users)
    User.save()


def convert_rests_to_sql(path):
    df = pd.read_csv(path)
    rests = []
    for i in range(len(df)):
        print(i)
        rests.append(Rest(
            rest_id=df.loc[i]['id'],
            address=df.loc[i]['adress'],
            name=df.loc[i]['name'],
            name_a=df.loc[i]['a_name']
        ))
    Rest.objects.bulk_create(rests)
    Rest.save()
    time.sleep(5000)


# convert_rests_to_sql(RESTS_PATH)

convert_user_to_sql(USERS_PATH)