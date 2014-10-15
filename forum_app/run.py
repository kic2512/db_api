__author__ = 'kic'

import flask
from flask import Flask, request, render_template

from forum_app.api_packs.forum_api.forum_urls import forum_urls
from forum_app.api_packs.forum_api.forum_create import create_forum

from forum_app.api_packs.user_api.user_urls import user_urls
from forum_app.api_packs.user_api.user_create import create_user

from forum_app.api_packs.thread_api.thread_urls import thread_urls
from forum_app.api_packs.thread_api.thread_create import create_thread
from forum_app.api_packs.thread_api.thread_close import close_thread
from forum_app.api_packs.thread_api.thread_remove import remove_thread
from forum_app.api_packs.thread_api.thread_open import open_thread

from forum_app.api_packs.post_api.post_urls import post_urls
from forum_app.api_packs.post_api.post_create import create_post
from forum_app.api_packs.post_api.post_remove import remove_post
from forum_app.api_packs.post_api.post_restore import restore_post
from forum_app.api_packs.post_api.post_update import update_post
from forum_app.api_packs.post_api.post_vote import vote_post

forum = Flask(__name__)


@forum.route(forum_urls['forum_create'], methods=['POST'])  # 1
def api_create_forum():
    data = flask.request.json
    return create_forum(data)


@forum.route(user_urls['user_create'], methods=['POST'])  # 2
def api_create_user():
    data = flask.request.json
    return create_user(data)


@forum.route(thread_urls['thread_create'], methods=['POST'])  # 3
def api_create_thread():
    data = flask.request.json
    return create_thread(data)


@forum.route(thread_urls['thread_close'], methods=['POST'])  # 4
def api_close_thread():
    data = flask.request.json
    return close_thread(data)


@forum.route(thread_urls['thread_open'], methods=['POST'])  # 5
def api_open_thread():
    data = flask.request.json
    return open_thread(data)


@forum.route(thread_urls['thread_remove'], methods=['POST'])  # 6
def api_remove_thread():
    data = flask.request.json
    return remove_thread(data)


@forum.route(post_urls['post_create'], methods=['POST'])  # 7
def api_create_post():
    data = flask.request.json
    return create_post(data)


@forum.route(post_urls['post_remove'], methods=['POST'])  # 8
def api_remove_post():
    data = flask.request.json
    return remove_post(data)


@forum.route(post_urls['post_restore'], methods=['POST'])  # 9
def api_restore_post():
    data = flask.request.json
    return restore_post(data)


@forum.route(post_urls['post_update'], methods=['POST'])  # 10
def api_update_post():
    data = flask.request.json
    return update_post(data)


@forum.route(post_urls['post_vote'], methods=['POST'])  # 10
def api_vote_post():
    data = flask.request.json
    return vote_post(data)


@forum.route('/')
def lal():
    return "New 1 !"


@forum.route('/index/')
def index():
    return render_template('test.html')


if __name__ == '__main__':
    forum.run(debug='True')
