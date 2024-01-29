import configuration
import requests
import data


def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.order_body)


def get_orders_track(track_id):
    return requests.get(configuration.URL_SERVICE + configuration.RECEIVING_AN_ORDER_BY_NUMBER + str(track_id))