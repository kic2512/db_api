__author__ = 'kic'

import flask
from forum_app.api_packs.db_queries.queries import exec_sql, open_sql, build_sql_insert_query, \
    build_sql_select_all_query
from forum_app.api_packs.make_response.make_response import make_response
from forum_app.api_packs.user_api.user_details import get_details_user


def create_forum(data):
    code = 0
    keys = ['id', 'name', 'short_name', 'user']
    if not data:
        values = [1, 'name', 'shn', 'email']
        resp_dict = make_response(keys, values, code=0, sql='Forum: Data not found')
        return flask.jsonify(resp_dict)

    name = data['name'].encode("utf-8")
    shn = data['short_name'].encode("utf-8")
    email = data['user'].encode("utf-8")

    sql_scheme = {
        'columns_names': ['name'],
        'columns_values': [name],
        'table': 'Forum'
    }

    sql_check = build_sql_select_all_query(sql_scheme, limit=1, what=' id ')

    res = open_sql(sql_check)  # check if exists

    if not res:
        sql_scheme = {
            'columns_names': ['name', 'short_name', 'user'],
            'columns_values': [name, shn, email],
            'table': 'Forum'
        }

        sql = build_sql_insert_query(sql_scheme)
        exec_message = exec_sql(sql)
        if exec_message == 0:
            res = open_sql(sql_check)
        else:
            #code = 4
            a = 0
    if res and res != -1:
        values = [int(res['id']), name, shn, email]
    else:
        values = [1, name, shn, email]
        #code = 4
    resp_dict = make_response(keys, values, code, sql_check)
    return flask.jsonify(resp_dict)