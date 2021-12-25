from django.shortcuts import render, redirect
from . import validatior, list_preparation
from graduation_website import cache
from . import mappers
from . import models

# from . import data_converter
DEFAULT_DISH_IMG_URL = 'pic/p-3.jpg'
DEFAULT_REST_IMG_URL = 'pic/p-3.jpg'


def start(request):
    # request.session.clear()
    if request.session.get('logged', False):
        return redirect(mappers.application_strategy[cache.ACTIVE_APPLICATION_STRATEGY.key]['first_page'])
    else:
        return redirect('/login')


def get_first_list_page(request):
    if request.session.get('logged', False):
        try:
            url = cache.ACTIVE_MARKETING_STRATEGY.url
            # dishes is dict
            # dishes keys: dish_rest, dish_similar, dish_famous

            dishes = list_preparation.first_menu_prepare(request, request.session['user_id'], request.session['time'],
                                                         url)

            global DEFAULT_DISH_IMG_URL
            # normalization (name and image url)
            for type in dishes.keys():
                for i in range(len(dishes[type])):
                    if not dishes[type][i].img_url:
                        dishes[type][i].img_url = DEFAULT_DISH_IMG_URL
                    dishes[type][i].dish_name = dishes[type][i].dish_name[1:-1]
        except Exception as ex:
            print('Exception:', ex)
            dishes = {}
        return render(request, "first_list_dishes_home.html",
                      dishes)
    return redirect('/login')


def get_rests_list(request):
    if request.session.get('logged', False):
        url = cache.ACTIVE_MARKETING_STRATEGY.url
        try:

            rests = list_preparation.rests_list_prepare(request.session['user_id'], request.session['time'], url)
        except Exception as ex:
            print('Exception', ex)
            rests = []

        global DEFAULT_REST_IMG_URL
        for i in range(len(rests)):
            if not rests[i].img:
                rests[i].img = DEFAULT_REST_IMG_URL

        return render(request, 'restaurant.html', {'rests': rests, 'user_address': request.session.get('address', '')})
    return redirect('/login')


def get_rest_dishes(request, id):
    if request.session.get('logged', False):
        url = 'rank_dish_request'
        try:
            # dishes keys: dish_rest, dish_similar, dish_famous
            dishes = list_preparation.rest_menu_prepare(request=request, rest_id=id, time=request.session['time'],
                                                        user_id=request.session['user_id'], url=url)
            # normalization (name and image url)
            for type in dishes.keys():
                for i in range(len(dishes[type])):
                    if not dishes[type][i].img_url:
                        dishes[type][i].img_url = DEFAULT_DISH_IMG_URL
                    dishes[type][i].dish_name = dishes[type][i].dish_name[1:-1]
        except Exception as ex:
            print('Exception:', ex)
            dishes = {}
        return render(request, 'first_list_dishes.html', dishes)
    return redirect('/login')


def get_related_dishes(request, dish_id):
    if request.session.get('logged', False):
        url = 'related_dishs'
        try:
            dishes = list_preparation.related_menu_prepare(request, dish_id, url)
            # normalization (name and image url)
            for i in range(len(dishes)):
                if not dishes[i].img_url:
                    dishes[i].img_url = DEFAULT_DISH_IMG_URL
                dishes[i].dish_name = dishes[i].dish_name[1:-1]
        except Exception as ex:
            print('Exception:', ex)
            dishes = []
        return render(request, "related_dishes_page.html",
                      {"dishes": dishes, 'home': '/dishes', 'user_address': request.session.get('address', '')})
    return redirect('/login')


def get_related_dishes_2(request, id_1, id_2):
    if request.session.get('logged', False):
        url = 'related_dishs'
        try:
            dishes = list_preparation.related_menu_prepare(request, id_2, url)

            # normalization (name and image url)
            for i in range(len(dishes)):
                if not dishes[i].img_url:
                    dishes[i].img_url = DEFAULT_DISH_IMG_URL
                dishes[i].dish_name = dishes[i].dish_name[1:-1]
        except Exception as ex:
            print('Exception:', ex)
            dishes = []
        return render(request, "related_dishes_page.html",
                      {"dishes": dishes, 'home': '/home', 'user_address': request.session.get('address', '')})
    return redirect('/login')


def show_index(request):
    return render(request, 'index_11.html')


def login(request):
    if request.method == 'POST':
        # the method is post.
        user_id = request.POST['id']
        time = request.POST['time']
        # some validation process on id and date.
        user = validatior.user_id_validation(user_id)
        if user:
            request.session['user_id'] = user_id
            request.session['time'] = time
            request.session['address'] = user.address
            request.session['logged'] = True
            return redirect(mappers.application_strategy[cache.ACTIVE_APPLICATION_STRATEGY.key]['first_page'])
    return render(request, 'form.html')
