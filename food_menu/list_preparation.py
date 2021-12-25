from .models import Order, Dish, Rest
from . import recommander_connector


def first_menu_prepare(request, user_id, time, url):
    orders_list = Order.objects.filter(user_id=user_id).order_by('-order_time')[:3]
    dish_id_list = [float(o.dish_id) for o in orders_list]

    time = ' '.join(time.split('T')) + ':00'

    request_parameters = {
        "user_id": float(user_id),
        "time": time,
        "previos_dishs": dish_id_list
    }
    try:
        # request from api
        response_data = recommander_connector.request_from_api(request_parameters, url)['dishs_ids']
        try:
            request.session['similar'] = response_data['dish_similar']
        except Exception as ex:
            print('In Session:', ex)
        # normalize dishes:
        dishes = dishes_ids_to_dishes(response_data)
    except Exception as ex:
        dishes = {}
        print('Exception in First-Menu: ', ex)
    return dishes


def related_menu_prepare(request, ordered_dish, url):
    # get related dishes from api.
    request_parameters = {
        "dish_id": ordered_dish,
    }
    try:
        # request from api
        response_data = recommander_connector.request_from_api(request_parameters, url)["result"]
        # don't have related:
        # if 0 <= len(response_data) <= 5:
        #     response_data += request.session['similar']
        # normalize dishes:
        dishes = dishes_ids_to_dishes(response_data)
    except Exception as ex:
        dishes = {}
        print('Exception in Related-Menu: ', ex)

    return dishes


def rest_menu_prepare(request, rest_id, time, user_id, url):
    orders_list = Order.objects.filter(user_id=user_id).order_by('-order_time')[:3]
    dish_id_list = [float(o.dish_id) for o in orders_list]

    time = ' '.join(time.split('T')) + ':00'

    request_parameters = {
        "rest_id": float(rest_id),
        "time": time,
        "previos_dishs": dish_id_list
    }
    try:
        # request from api
        response_data = recommander_connector.request_from_api(request_parameters, url)['dishs_ids']
        try:
            request.session['similar'] = response_data['dish_similar']
        except Exception as ex:
            print('In Session:', ex)
        # normalize dishes:
        dishes = dishes_ids_to_dishes(response_data)
    except Exception as ex:
        dishes = {}
        print('Exception in Rest-Menu: ', ex)
    return dishes


def rests_list_prepare(user_id, time, url):
    orders_list = Order.objects.filter(user_id=user_id).order_by('-order_time')[:3]
    dish_id_list = [float(o.dish_id) for o in orders_list]

    time = ' '.join(time.split('T')) + ':00'
    print('user_id: ', user_id)
    request_parameters = {
        "user_id": float(user_id),
        "time": time,
        "previos_dishs": dish_id_list
    }
    try:
        # request from api
        rests_ids = recommander_connector.request_from_api(request_parameters, url)['ids_rests']
        # normalize rests
        recommended_rests = rests_ids_to_rests(rests_ids)
    except Exception as ex:
        print('Exception in Rests-List', ex)
        recommended_rests = []
    return recommended_rests


def dishes_ids_to_dishes(dishes_ids: dict):
    dishes = {}
    try:
        if isinstance(dishes_ids, dict):
            for dish_type in dishes_ids.keys():
                dishes[dish_type] = Dish.objects.filter(dish_id__in=[int(i) for i in dishes_ids[dish_type]])
        elif isinstance(dishes_ids, list):
            dishes = Dish.objects.filter(dish_id__in=[int(i) for i in dishes_ids])
    except Exception as ex:
        print('Exception dishes id: ', ex)

    return dishes


def rests_ids_to_rests(rest_ids: list):
    try:
        return Rest.objects.filter(rest_id__in=[int(i) for i in rest_ids])
    except Exception as ex:
        return []
