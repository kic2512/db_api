__author__ = 'kic'

import flask
from forum_app.api_packs.make_response.make_response import make_response
from forum_app.api_packs.db_queries.queries import exec_sql, open_sql, build_sql_select_all_query, \
    build_sql_update_query


def open_thread(data):
    code = 0
    thread = data['thread']

    sql_scheme = {
        'columns_names': ['id'],
        'columns_values': [thread],
        'table': 'Thread'
    }

    sql_check = build_sql_select_all_query(sql_scheme)
    res = open_sql(sql_check)
    if res:
        sql_scheme = {
            'columns_names': ['isClosed'],
            'columns_values': [0],
            'condition': {'id': thread},
            'table': 'Thread'
        }

        exec_message = exec_sql(build_sql_update_query(sql_scheme))
        if exec_message != 0:
            code = 4
    else:
        code = 1

    keys = ['thread']
    values = [thread]

    resp_dict = make_response(keys, values, code)
    return flask.jsonify(resp_dict)
