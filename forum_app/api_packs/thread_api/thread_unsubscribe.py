__author__ = 'kic'

import flask
from forum_app.api_packs.db_queries.queries import exec_sql, open_sql, build_sql_select_all_query, \
    build_sql_update_query
from forum_app.api_packs.make_response.make_response import make_response


def unsubscribe_thread(data):
    code = 0
    keys = []
    values = []

    thread_id = data['thread']
    email = data['user']

    sql_scheme = {
        'columns_names': ['thread', 'user'],
        'columns_values': [thread_id, email],
        'table': 'Subscribe'
    }

    sql_check = build_sql_select_all_query(sql_scheme)

    res = open_sql(sql_check)  # check if exists

    if res:
        sql_scheme = {
            'columns_names': ['isDeleted'],
            'columns_values': [1],
            'condition': {'id': res['id']},
            'table': 'Subscribe'
        }
        exec_sql(build_sql_update_query(sql_scheme))

        keys = ['thread', 'user']

        values = [res['thread'], res['user']]

    else:
        code = 1

    resp_dict = make_response(keys=keys, values=values, code=code)
    return flask.jsonify(resp_dict)