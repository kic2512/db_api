__author__ = 'kic'

import json
import flask
from flask import Flask, request, render_template, make_response

from forum_app.api_packs.db_queries.queries import exec_sql, open_sql
from forum_app.api_packs.forum_api.forum_func import get_forum_response
from forum_app.api_packs.forum_api.forum_urls import forum_urls

from forum_app.api_packs.user_api.user_urls import user_urls
from forum_app.api_packs.user_api.user_func import get_user_response

forum = Flask(__name__)


@forum.route(forum_urls['forum_create'], methods=['GET', 'POST'])
def api_create_forum():
    if request.method == 'POST':
        data = flask.request.json  # json.loads(create_forum_request)

        name = data['name']
        shn = data['short_name']
        usr = data['user']

        sql_check = "select id,name,short_name,user from Forum where name = '%s' and short_name = '%s' " % (name, shn)

        res = open_sql(sql_check)  # check if exists

        if not res:
            sql = "insert into Forum (name,short_name,user) values('%s','%s','%s')" % (name, shn, usr)
            res = exec_sql(sql)
            if res == 0:
                res = open_sql(sql_check)
            else:
                TODO = None

        resp_dict = get_forum_response(fid=int(res[0][0]), name=res[0][1], short_name=res[0][2], user=res[0][3])
        # j_dict = json.dumps(resp_dict)
        # response = make_response(j_dict)

        return flask.jsonify(resp_dict)

    return "Do not make a GET"


@forum.route(user_urls['user_create'], methods=['GET', 'POST'])
def api_create_user():
    if request.method == 'POST':
        data = flask.request.json  # json.loads(create_forum_request)

        username = data['username']
        about = data['about']
        name = data['name']
        email = data['email']
        if 'isAnonymous' in data:
            isanon = data['isAnonymous']
        else:
            isanon = 'False'

        sql_check = "select id, username, about, name, email, isAnonymous from User where email = '%s' " % email

        res = open_sql(sql_check)  # check if exists

        if not res:
            sql = "insert into User (username, about, name, email, isAnonymous) values('%s','%s','%s','%s','%s')" % (
                username, about, name, email, isanon)

            res = exec_sql(sql)
            if res == 0:
                res = open_sql(sql_check)
            else:
                TODO = None
        resp_dict = get_user_response(uid=int(res[0][0]), username=res[0][1], about=res[0][2], name=res[0][3],
                                      email=res[0][4], isanonymous=isanon)

        return flask.jsonify(resp_dict)

    return "Do not make a GET"


@forum.route('/')
def lal():
    return "New 1 !"


@forum.route('/index/')
def index():
    return render_template('test.html')


if __name__ == '__main__':
    forum.run(debug='True')
