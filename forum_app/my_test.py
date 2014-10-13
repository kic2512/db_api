__author__ = 'kic'
import requests
import json


def forum_create():
    dict = {'name': u'\u0424\u043e\u0440\u0443\u043c \u0422\u0440\u0438', 'short_name': 'forum3',
            'user': 'richard.nixon@example.com'}
    host = "http://127.0.0.1/db/api/forum/create/"
    response = requests.post(host, data=json.dumps(dict), headers={'content-type': 'application/json'})
    print response.text


def user_create():
    dict = {'username': 'user1', 'about': 'hello im user1', 'isAnonymous': True, 'name': 'John',
            'email': 'example@mail.ru'}
    host = "http://127.0.0.1/db/api/user/create/"
    response = requests.post(host, data=json.dumps(dict), headers={'content-type': 'application/json'})
    print response.text


def thread_create():
    dict = {'forum': 'forum1', 'title': u'ee', 'isClosed': False,
            'user': 'example2@mail.ru', 'date': '2013-12-29 00:01:01', 'message': 'hey hey hey!', 'slug': 'thread3',
            'isDeleted': False}
    host = "http://127.0.0.1/db/api/thread/create/"
    response = requests.post(host, data=json.dumps(dict), headers={'content-type': 'application/json'})
    print response.text


def post_create():
    dict = {"isApproved": True, "user": "example@mail.ru", "date": "2014-01-01 00:00:01", "message": "my message 1",
            "isSpam": False, "isHighlighted": True, "thread": 4, "forum": "forum2", "isDeleted": False,
            "isEdited": False}
    host = "http://127.0.0.1/db/api/post/create/"
    response = requests.post(host, data=json.dumps(dict), headers={'content-type': 'application/json'})
    print response.text


forum_create()
user_create()
thread_create()
post_create()

