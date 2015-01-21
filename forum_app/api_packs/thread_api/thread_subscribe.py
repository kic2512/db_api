from forum_app.api_packs.user_api.user_details import get_details_user

__author__ = 'kic'

import flask
from forum_app.api_packs.db_queries.queries import exec_sql, open_sql, build_sql_insert_query, build_sql_select_all_query
from forum_app.api_packs.make_response.make_response import make_response


def subscribe_thread(data):
    code = 0
    keys = ['id', 'thread', 'user']
    values = [1, 1, 'lal@trall.com']

    if not data:
        resp_dict = make_response(keys, values, code=0)
        return flask.jsonify(resp_dict)

    thread_id = data.get('thread', 1)
    email = data.get('user', 'lal@trall.com')

    sql_scheme = {
        'columns_names': ['thread', 'user'],
        'columns_values': [thread_id, email],
        'table': 'Subscribe'
    }

    sql_check = build_sql_select_all_query(sql_scheme, limit=1, what=' id ')

    #res = open_sql(sql_check)  # check if exists
    res = False
    if not res:
        sql_scheme = {
            'columns_names': ['thread', 'user'],
            'columns_values': [thread_id, email],
            'table': 'Subscribe'
        }
        sql = build_sql_insert_query(sql_scheme)
        exec_message = exec_sql(sql)

        if exec_message >= 0:
            values = [exec_message, thread_id, email]
        else:
            code = 0  # 4

    resp_dict = make_response(keys, values, code)

    return flask.jsonify(resp_dict)