__author__ = 'kic'
import requests
import json


def forum_create():
    d = {'name': u'\u0424\u043e\u0440\u0443\u043c \u0422\u0440\u0438', 'short_name': 'forum3',
            'user': 'richard.nixon@example.com'}
    host = "http://127.0.0.1/db/api/forum/create/"
    response = requests.post(host, data=json.dumps(d), headers={'content-type': 'application/json'})
    print response.text


def forum_details():
    host = "http://127.0.0.1/db/api/forum/details/?related=user&forum=forum1"
    response = requests.get(host)
    print response.text


def user_create():
    d = {'username': None, 'about': 'hello im user1', 'isAnonymous': True, 'name': 'John',
            'email': 'example2@mail.ru'}
    host = "http://127.0.0.1/db/api/user/create/"
    response = requests.post(host, data=json.dumps(d), headers={'content-type': 'application/json'})
    print response.text


def user_details():
    host = "http://127.0.0.1/db/api/user/details/?user=richard.nixon@example.com"
    response = requests.get(host)
    print response.text


def thread_create():
    d = {'forum': 'forum3', 'title': u'\u0422\u0440\u0435\u0434 \u0422\u0440\u0438', 'isClosed': False,
            'user': 'example2@mail.ru', 'date': '2013-12-29 00:01:01', 'message': 'hey hey hey!', 'slug': 'thread3',
            'isDeleted': False}
    host = "http://127.0.0.1/db/api/thread/create/"
    response = requests.post(host, data=json.dumps(d), headers={'content-type': 'application/json'})
    print response.text


def thread_details():
    host = "http://127.0.0.1/db/api/thread/details/?thread=1&related=forum&related=user"
    response = requests.get(host)
    print response.text


def post_create():
    d = {"isApproved": True, "user": "example2@mail.ru", "date": "2014-01-01 00:00:01", "message": "my message 1",
            "isSpam": False, "isHighlighted": True, "thread": 1, "forum": "forum2", "isDeleted": False,
            "isEdited": False}
    host = "http://127.0.0.1/db/api/post/create/"
    response = requests.post(host, data=json.dumps(d), headers={'content-type': 'application/json'})
    print response.text


def post_details():
    host = "http://127.0.0.1/db/api/post/details/?post=1&related=forum"
    response = requests.get(host)
    print response.text


def thread_close():
    d = {'thread': 1}
    host = "http://127.0.0.1/db/api/thread/close/"
    response = requests.post(host, data=json.dumps(d), headers={'content-type': 'application/json'})
    print response.text


def post_remove():
    d = {'post': 1}
    host = "http://127.0.0.1/db/api/post/remove/"
    response = requests.post(host, data=json.dumps(d), headers={'content-type': 'application/json'})
    print response.text


def post_vote():
    d = {'post': 1, 'vote': 1}
    host = "http://127.0.0.1/db/api/post/vote/"
    response = requests.post(host, data=json.dumps(d), headers={'content-type': 'application/json'})
    print response.text


def post_update():
    d = {"post": 3, "message": "my message 1 LALALA"}
    host = "http://127.0.0.1/db/api/post/update/"
    response = requests.post(host, data=json.dumps(d), headers={'content-type': 'application/json'})
    print response.text


def post_restore():
    d = {'post': 2}
    host = "http://127.0.0.1/db/api/post/restore/"
    response = requests.post(host, data=json.dumps(d), headers={'content-type': 'application/json'})
    print response.text


def thread_remove():
    d = {'thread': 1}
    host = "http://127.0.0.1/db/api/thread/remove/"
    response = requests.post(host, data=json.dumps(d), headers={'content-type': 'application/json'})
    print response.text


def thread_restore():
    d = {'thread': 1}
    host = "http://127.0.0.1/db/api/thread/restore/"
    response = requests.post(host, data=json.dumps(d), headers={'content-type': 'application/json'})
    print response.text


def thread_open():
    d = {'thread': 1}
    host = "http://127.0.0.1/db/api/thread/open/"
    response = requests.post(host, data=json.dumps(d), headers={'content-type': 'application/json'})
    print response.text


def clear():
    d = {}
    host = "http://127.0.0.1/db/api/clear/"
    response = requests.post(host, data=json.dumps(d), headers={'content-type': 'application/json'})
    print response.text

post_vote()