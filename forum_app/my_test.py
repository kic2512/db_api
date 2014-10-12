__author__ = 'kic'
import requests
import json


def forum_create():
    dict = {'name': u'\u0424\u043e\u0440\u0443\u043c \u0422\u0440\u0438', 'short_name': 'forum3', 'user': 'richard.nixon@example.com'}
    host = "http://127.0.0.1/db/api/forum/create/"
    response = requests.post(host, data=json.dumps(dict), headers={'content-type': 'application/json'})
    print response.text


def user_create():
    dict = {'username': 'user1', 'about': 'hello im user1', 'isAnonymous': False, 'name': 'John',
            'email': 'example@mail.ru'}
    host = "http://127.0.0.1/db/api/user/create/"
    response = requests.post(host, data=json.dumps(dict), headers={'content-type': 'application/json'})
    print response.text

forum_create()
user_create()

