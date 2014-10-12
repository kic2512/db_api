__author__ = 'kic'
import urllib2
import requests
import json


def forum_create():
    dict = {'name': 'Forum With Sufficiently Large Name', 'short_name': 'forumwithsufficientlylargename',
            'user': 'test@test.com'}
    host = "http://127.0.0.1/db/api/user/create/"
    response = requests.post(host, data=json.dumps(dict), headers={'content-type': 'application/json'})
    print response.text


def user_create():
    dict = {"username": "user1", "about": "hello im user1", "isAnonymous": False, "name": "John",
            "email": "example@mail.ru"}
    host = "http://127.0.0.1/db/api/user/create/"
    response = requests.post(host, data=json.dumps(dict), headers={'content-type': 'application/json'})
    print response.text


user_create()

