__author__ = 'kic'

import flask
from forum_app.api_packs.db_queries.queries import exec_sql, open_sql, build_sql_query
from forum_app.api_packs.make_response.make_response import make_response


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
        sql_scheme = {
            'columns_names': ['username', 'about', 'name', 'email', 'isAnonymous'],
            'columns_values': [str(username), str(about), str(name), str(email), str(isanon)],
            'table': 'User',
            'type': 'insert'}

        sql = build_sql_query(sql_scheme)
        res = exec_sql(sql)

        if res == 0:
            res = open_sql(sql_check)
        else:
            TODO = None

    keys = ['id', 'username', 'about', 'name', 'email', 'isAnonymous']
    values = [int(res['id']), res['username'], res['about'], res['name'], res['email'], bool(res['isAnonymous'])]

    resp_dict = make_response(keys, values)

    return flask.jsonify(resp_dict)