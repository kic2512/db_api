__author__ = 'kic'

import flask
from forum_app.api_packs.db_queries.queries import exec_sql, open_sql, build_sql_insert_query, \
    build_sql_select_all_query
from forum_app.api_packs.make_response.make_response import make_response


def get_details_user(data):
    code = 0

    email = data['user'][0]
    sql_scheme = {
        'columns_names': ['email'],
        'columns_values': [email],
        'table': 'User'
    }

    sql_check = build_sql_select_all_query(sql_scheme)
    res = open_sql(sql_check)  # check if exists

    if not res:
        code = 5
    else:
        keys = ['about', 'email', 'followers', 'following', 'id', 'isAnonymous', 'name', 'subscriptions', 'username']
        values = [res['about'], res['email'], [], [], int(res['id']), bool(res['isAnonymous']), res['name'],
                  [], res['username']]

    resp_dict = make_response(keys, values, code)

    return resp_dict
