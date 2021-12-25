from django.http import JsonResponse
from django.shortcuts import render, redirect

from food_menu.models import Rest
from .models import UserExperienceStrategy, MarketingStrategy
from . import statistics_controller
from . import mappers
import json

DEFAULT_DATE = '2020-04-1 00:00:00'


def start(request):
    return redirect('/home')


def login(request):
    pass


def strategies_page(request):
    if request.method == 'POST':
        try:
            if request.is_ajax():
                key = request.POST.get('key', None)
                updated = request.POST.get('updated', None)

                # update strategy:
                if key:
                    mappers.update_strategy[updated](key)
                else:
                    request.session['date'] = request.POST.get('date', None)
                    return JsonResponse({'success': True, 'url': '/manager/home'})
        except:
            print('k' * 30)

    try:
        marketing_strategies = MarketingStrategy.objects.all()
        user_strategies = UserExperienceStrategy.objects.all()
    except:
        marketing_strategies = []
        user_strategies = []
    try:
        print('date is:',request.session.get('date'))
        url = 'sale_per_month_place'
        sales_per_month = statistics_controller.get_sales_per_month(request.session.get('date', DEFAULT_DATE), url)
        url = 'get_most_popular_restaurants'
        most_popular_rests = statistics_controller.get_most_popular_rests(request.session.get('date', DEFAULT_DATE), url)
    except Exception as ex:
        print('Exception:', ex)
        sales_per_month = {}
        most_popular_rests = {}

    return render(request, 'home.html', {
        'm_strategies': marketing_strategies,
        'u_strategies': user_strategies,
        'sales_per_month': json.dumps(sales_per_month),
        'most_popular_rests': json.dumps(most_popular_rests)
    })


def get_rest(request):
    return render(request, 'home.html')
