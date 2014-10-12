__author__ = 'kic'

import flask
from flask import Flask, request, render_template

from forum_app.api_packs.forum_api.forum_urls import forum_urls
from forum_app.api_packs.forum_api.forum_create import create_forum

from forum_app.api_packs.user_api.user_urls import user_urls
from forum_app.api_packs.user_api.user_create import create_user


forum = Flask(__name__)


@forum.route(forum_urls['forum_create'], methods=['GET', 'POST'])
def api_create_forum():
    if request.method == 'POST':
        data = flask.request.json
        return create_forum(data)

    return 'Do not GET request'


@forum.route(user_urls['user_create'], methods=['GET', 'POST'])
def api_create_user():
    if request.method == 'POST':

        data = flask.request.json
        return create_user(data)

    return "Do not make a GET"


@forum.route('/')
def lal():
    return "New 1 !"


@forum.route('/index/')
def index():
    return render_template('test.html')


if __name__ == '__main__':
    forum.run(debug='True')
