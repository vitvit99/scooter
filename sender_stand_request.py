import configuration
import data
import requests


def post_new_order():   # Создание заказа
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=data.order_body)


def get_track_number():   # Получение трек номера
    return post_new_order().json()["track"]


def get_order():   # Получение заказа по его номеру
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER + "{}".format(get_track_number())
                        )
