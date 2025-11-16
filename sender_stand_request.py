import configuration
import requests
import data

# def post_new_order(body):
#     return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
#                          json=body,
#                          headers=data.headers)

def post_create_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=data.order_body)

def get_receiving_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.RECEIVING_ORDER.format(track))