from . import views

application_strategy = {
    'rest_based': {
        'first_page': '/home',
        'second_page': '/dishes',
        'third_page': '/related'
    },
    'dish_based': {
        'first_page': '/dishes',
        'second_page': '/dishes',
        'third_page': '/related'
    }
}

market_strategy = {}
