import requests

recommender_api_url = "http://127.0.0.1:8000/"


def request_from_api(parameters, url):
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        response = requests.request("GET", recommender_api_url+url, headers=headers, json=parameters)
        response_data = response.json()
    except Exception as ex:
        print('Empty List', ex)
        response_data = {}
    return response_data
