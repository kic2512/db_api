__author__ = 'kic'

import flask
from forum_app.api_packs.db_queries.queries import exec_sql, open_sql, build_sql_select_all_query, \
    build_sql_update_query, open_sql_all
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

    res_dict = open_sql_all(sql_check, first=True, is_closing=False)  # check if exists
    res = res_dict['result'][0]
    if res == -1 or not res:
        return make_response([], [], code=4)
    db = res_dict['db']
    crs = res_dict['cursor']

    if res:
        sql_scheme = {
            'columns_names': ['isDeleted'],
            'columns_values': [1],
            'condition': {'id': res['id']},
            'table': 'Subscribe'
        }
        exec_sql(build_sql_update_query(sql_scheme), first=False, cursor=crs, is_closing=False)

        keys = ['thread', 'user']
        values = [res['thread'], res['user']]

    else:
        code = 1

    db.close()
    resp_dict = make_response(keys=keys, values=values, code=code)
    return flask.jsonify(resp_dict)