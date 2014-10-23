from forum_app.api_packs.user_api.user_details import get_details_user

__author__ = 'kic'

import flask
from forum_app.api_packs.db_queries.queries import exec_sql, open_sql, build_sql_insert_query, build_sql_select_all_query
from forum_app.api_packs.make_response.make_response import make_response


def subscribe_thread(data):
    code = 0
    thread_id = data['thread']
    email = data['user']

    usr_details = get_details_user({'user': [email, ]})['response']
    usr_id = usr_details['id']

    sql_scheme = {
        'columns_names': ['thread', 'user'],
        'columns_values': [thread_id, usr_id],
        'table': 'Subscribe'
    }

    sql_check = build_sql_select_all_query(sql_scheme)

    res = open_sql(sql_check)  # check if exists

    if not res:
        sql_scheme = {
            'columns_names': ['thread', 'user'],
            'columns_values': [thread_id, usr_id],
            'table': 'Subscribe'
        }
        sql = build_sql_insert_query(sql_scheme)
        exec_message = exec_sql(sql)

        if exec_message == 0:
            res = open_sql(sql_check)
        else:
            code = 4

    keys = ['thread', 'user']
    values = [res['thread'], res['user']]

    resp_dict = make_response(keys, values, code)

    return flask.jsonify(resp_dict)

