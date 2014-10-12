__author__ = 'kic'

import flask
from forum_app.api_packs.db_queries.queries import exec_sql, open_sql
from forum_app.api_packs.user_api.user_func import get_user_response


def create_user(data):
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
    resp_dict = get_user_response(uid=int(res['id']), username=res['username'], about=res['about'], name=res['name'],
                                  email=res['email'], isanonymous=bool(res['isAnonymous']))

    return flask.jsonify(resp_dict)