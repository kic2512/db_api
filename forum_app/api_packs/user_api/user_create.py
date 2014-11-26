__author__ = 'kic'

import flask
from forum_app.api_packs.db_queries.queries import exec_sql, open_sql, build_sql_insert_query, \
    build_sql_select_all_query
from forum_app.api_packs.make_response.make_response import make_response


def create_user(data):
    code = 0

    username = data['username']
    about = data['about']
    name = data['name']
    email = data['email']

    if 'isAnonymous' in data:
        isanon = data['isAnonymous']
    else:
        isanon = 'False'

    sql_scheme = {
        'columns_names': ['email'],
        'columns_values': [email],
        'table': 'User'
    }

    sql_check = build_sql_select_all_query(sql_scheme)

    res = open_sql(sql_check)  # check if exists

    if not res:
        sql_scheme = {
            'columns_names': ['username', 'about', 'name', 'email', 'isAnonymous'],
            'columns_values': [username, about, name, email, int(isanon)],
            #'modify': []
            'table': 'User'
        }
        sql = build_sql_insert_query(sql_scheme)
        exec_message = exec_sql(sql)

        if exec_message == 0:
            res = open_sql(sql_check)
        else:
            code = 4
    else:
        code = 5

    keys = ['id', 'username', 'about', 'name', 'email', 'isAnonymous']
    values = [int(res['id']), res['username'], res['about'], res['name'], res['email'], bool(res['isAnonymous'])]

    resp_dict = make_response(keys, values, code)

    return flask.jsonify(resp_dict)