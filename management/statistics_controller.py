from food_menu import recommander_connector
from food_menu import models as food_models

import pandas as pd


def month_date_splitter(datetime):
    try:
        return "-".join(i for i in datetime.split(' ')[0].split('-')[0:2])
    except Exception as ex:
        print('Not Supported Format>', ex)
        return ''


def get_sales_per_month(datetime, url):
    month_date = month_date_splitter(datetime)
    request_data = {
        '': ''
    }
    try:
        response_data = recommander_connector.request_from_api(parameters=request_data, url=url)['result']
        sales = pd.DataFrame(response_data['data'])
        sales_per_month = sales[sales['month'] == month_date]
        return sales_per_month.to_dict(orient="list")
    except Exception as ex:
        print('Exception: ', ex)
        return pd.DataFrame(columns=['month', 'sales', 'place']).to_dict(orient="list")


def get_most_popular_rests(datetime, url):
    def get_rest_name(rest_id):
        try:
            return food_models.Rest.objects.filter(rest_id=rest_id).first().name_a
        except Exception as ex:
            return 'rest'
    month_date = month_date_splitter(datetime)
    request_data = {
        'month': month_date
    }
    try:
        response_data = recommander_connector.request_from_api(parameters=request_data, url=url)
        most_popular = pd.DataFrame(response_data['data'])
        most_popular['name'] = most_popular.rest_id.apply(get_rest_name)
        return most_popular.to_dict(orient="list")
    except Exception as ex:
        print('Exception: ', ex)
        return pd.DataFrame(columns=['rest_id', 'name', 'orders']).to_dict(orient="list")
