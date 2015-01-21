__author__ = 'kic'

import flask
from forum_app.api_packs.db_queries.queries import exec_sql, open_sql, build_sql_insert_query, \
    build_sql_select_all_query
from forum_app.api_packs.make_response.make_response import make_response


def create_user(data):
    code = 0
    keys = ['id', 'username', 'about', 'name', 'email', 'isAnonymous']
    values = [1, 'username', 'about', 'name', 'email', 'isanon']

    if not data:
        resp_dict = make_response(keys, values, code=0, sql='User: Data not found')
        return flask.jsonify(resp_dict)

    username = data['username']
    about = data['about']
    name = data['name']
    email = data['email']

    isanon = data.get('isAnonymous', False)

    sql_scheme = {
        'columns_names': ['email'],
        'columns_values': [email],
        'table': 'User'
    }

    sql_check = build_sql_select_all_query(sql_scheme, limit=1, what=' id ')

    #res = open_sql(sql_check)  # check if exists
    res = False
    if not res:
        sql_scheme = {
            'columns_names': ['username', 'about', 'name', 'email', 'isAnonymous'],
            'columns_values': [username, about, name, email, int(isanon)],
            'table': 'User'
        }
        sql = build_sql_insert_query(sql_scheme)
        exec_message = exec_sql(sql)
        if exec_message >= 0:
            #res = open_sql(sql_check)
            values = [exec_message, username, about, name, email, isanon]
        else:
            #code = 4
            a = 0
    else:
        #code = 5
        a = 0

    resp_dict = make_response(keys, values, code, sql_check)   # add this after load
    return flask.jsonify(resp_dict)    # add this after load