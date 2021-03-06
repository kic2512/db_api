from forum_app.api_packs.forum_api.forum_listPosts import get_forum_posts_list
from forum_app.api_packs.forum_api.forum_listThreads import get_forum_threads_list
from forum_app.api_packs.user_api.user_list_followers import get_user_list_followers
from forum_app.api_packs.user_api.user_list_following import get_user_list_following

__author__ = 'kic'

import flask
from flask import Flask, request, render_template

from forum_app.api_packs.forum_api.forum_urls import forum_urls
from forum_app.api_packs.forum_api.forum_create import create_forum
from forum_app.api_packs.forum_api.forum_details import get_details_forum
from forum_app.api_packs.forum_api.forum_listUsers import get_forum_users_list

from forum_app.api_packs.user_api.user_urls import user_urls
from forum_app.api_packs.user_api.user_create import create_user
from forum_app.api_packs.user_api.user_details import get_details_user
from forum_app.api_packs.user_api.user_listPosts import get_user_list_posts
from forum_app.api_packs.user_api.user_follow import follow_user
from forum_app.api_packs.user_api.user_unfollow import unfollow_user
from forum_app.api_packs.user_api.user_update import update_user


from forum_app.api_packs.thread_api.thread_urls import thread_urls
from forum_app.api_packs.thread_api.thread_create import create_thread
from forum_app.api_packs.thread_api.thread_close import close_thread
from forum_app.api_packs.thread_api.thread_remove import remove_thread
from forum_app.api_packs.thread_api.thread_open import open_thread
from forum_app.api_packs.thread_api.thread_details import get_details_thread
from forum_app.api_packs.thread_api.thread_restore import restore_thread
from forum_app.api_packs.thread_api.thread_update import update_thread
from forum_app.api_packs.thread_api.thread_listPosts import get_thread_list_posts
from forum_app.api_packs.thread_api.thread_vote import vote_thread
from forum_app.api_packs.thread_api.thread_list import get_thread_list
from forum_app.api_packs.thread_api.thread_subscribe import subscribe_thread
from forum_app.api_packs.thread_api.thread_unsubscribe import unsubscribe_thread


from forum_app.api_packs.post_api.post_urls import post_urls
from forum_app.api_packs.post_api.post_create import create_post
from forum_app.api_packs.post_api.post_remove import remove_post
from forum_app.api_packs.post_api.post_restore import restore_post
from forum_app.api_packs.post_api.post_update import update_post
from forum_app.api_packs.post_api.post_vote import vote_post
from forum_app.api_packs.post_api.post_details import get_details_post
from forum_app.api_packs.post_api.post_list import get_post_list


from forum_app.api_packs.clear import truncate_all

forum = Flask(__name__)


@forum.route('/db/api/clear/', methods=['POST'])  # 1.1
def api_clear():
    data = flask.request.json
    return flask.jsonify(truncate_all())


@forum.route(forum_urls['forum_create'], methods=['POST'])  # 1.1
def api_create_forum():
    data = flask.request.json
    return create_forum(data)


@forum.route(forum_urls['forum_details'], methods=['GET'])  # 1.2
def api_details_forum():
    data = dict(flask.request.args)
    return flask.jsonify(get_details_forum(data))


@forum.route(forum_urls['forum_listUsers'], methods=['GET'])  # 1.2
def api_list_users_forum():
    data = dict(flask.request.args)
    return flask.jsonify(get_forum_users_list(data))


@forum.route(forum_urls['forum_listPosts'], methods=['GET'])  # 1.2
def api_list_posts_forum():
    data = dict(flask.request.args)
    return flask.jsonify(get_forum_posts_list(data))


@forum.route(forum_urls['forum_listThreads'], methods=['GET'])  # 1.2
def api_list_threads_forum():
    data = dict(flask.request.args)
    return flask.jsonify(get_forum_threads_list(data))


@forum.route(user_urls['user_create'], methods=['POST'])  # 2.1
def api_create_user():
    data = flask.request.json
    return create_user(data)


@forum.route(user_urls['user_update'], methods=['POST'])  # 2.1
def api_update_user():
    data = flask.request.json
    return update_user(data)


@forum.route(user_urls['user_follow'], methods=['POST'])  # 2.1
def api_follow_user():
    data = flask.request.json
    return follow_user(data)


@forum.route(user_urls['user_unfollow'], methods=['POST'])  # 2.1
def api_unfollow_user():
    data = flask.request.json
    return unfollow_user(data)


@forum.route(user_urls['user_details'], methods=['GET'])  # 2.2
def api_details_user():
    data = dict(flask.request.args)
    return flask.jsonify(get_details_user(data))


@forum.route(user_urls['user_listPosts'], methods=['GET'])  # 2.2
def api_list_posts_user():
    data = dict(flask.request.args)
    return flask.jsonify(get_user_list_posts(data))


@forum.route(user_urls['user_list_followers'], methods=['GET'])  # 2.2
def api_list_followers_user():
    data = dict(flask.request.args)
    return flask.jsonify(get_user_list_followers(data))


@forum.route(user_urls['user_list_following'], methods=['GET'])  # 2.2
def api_list_following_user():
    data = dict(flask.request.args)
    return flask.jsonify(get_user_list_following(data))


@forum.route(thread_urls['thread_create'], methods=['POST'])  # 3
def api_create_thread():
    data = flask.request.json
    return create_thread(data)


@forum.route(thread_urls['thread_subscribe'], methods=['POST'])  # 3
def api_subscribe_thread():
    data = flask.request.json
    return subscribe_thread(data)


@forum.route(thread_urls['thread_unsubscribe'], methods=['POST'])  # 3
def api_unsubscribe_thread():
    data = flask.request.json
    return unsubscribe_thread(data)


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


@forum.route(thread_urls['thread_vote'], methods=['POST'])  # 6
def api_vote_thread():
    data = flask.request.json
    return vote_thread(data)


@forum.route(thread_urls['thread_restore'], methods=['POST'])  # 6
def api_restore_thread():
    data = flask.request.json
    return restore_thread(data)


@forum.route(thread_urls['thread_update'], methods=['POST'])  # 6
def api_update_thread():
    data = flask.request.json
    return update_thread(data)


@forum.route(thread_urls['thread_details'], methods=['GET'])  # 2.2
def api_details_thread():
    data = dict(flask.request.args)
    return flask.jsonify(get_details_thread(data))


@forum.route(thread_urls['thread_listPosts'], methods=['GET'])  # 2.2
def api_list_posts_thread():
    data = dict(flask.request.args)
    return flask.jsonify(get_thread_list_posts(data))


@forum.route(thread_urls['thread_list'], methods=['GET'])  # 2.2
def api_list_thread():
    data = dict(flask.request.args)
    return flask.jsonify(get_thread_list(data))


@forum.route(post_urls['post_create'], methods=['POST'])  # 7
def api_create_post():
    data = flask.request.json
    return create_post(data)


@forum.route(post_urls['post_details'], methods=['GET'])  # 7
def api_details_post():
    data = dict(flask.request.args)
    return flask.jsonify(get_details_post(data))


@forum.route(post_urls['post_list'], methods=['GET'])  # 7
def api_list_post():
    data = dict(flask.request.args)
    return flask.jsonify(get_post_list(data))


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
