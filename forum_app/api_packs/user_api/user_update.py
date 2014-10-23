from forum_app.api_packs.user_api.user_details import get_details_user

__author__ = 'kic'

import flask
from forum_app.api_packs.db_queries.queries import exec_sql, open_sql, build_sql_select_all_query, \
    build_sql_update_query
from forum_app.api_packs.make_response.make_response import make_response


def update_user(data):
    code = 0
    keys = []
    values = []

    about = data['about']
    user_email = data['user']
    name = data['name']

    sql_scheme = {
        'columns_names': ['email'],
        'columns_values': [user_email],
        'table': 'User'
    }

    sql_check = build_sql_select_all_query(sql_scheme)
    res = open_sql(sql_check)

    if res:
        sql_scheme = {
            'columns_names': ['name', 'about'],
            'columns_values': [name, about],
            'condition': {'email': user_email},
            'table': 'User'
        }
        exec_sql(build_sql_update_query(sql_scheme))

        user_data = {'user': [res['email'], ]}
        user_resp = get_details_user(user_data)['response']

    else:
        code = 1

    resp_dict = {'code': code, 'response': user_resp}
    return flask.jsonify(resp_dict)

