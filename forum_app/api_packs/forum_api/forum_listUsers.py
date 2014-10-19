__author__ = 'kic'

import flask
from forum_app.api_packs.db_queries.queries import exec_sql, open_sql, open_sql_all, build_sql_insert_query, \
    build_sql_select_all_query
from forum_app.api_packs.make_response.make_response import make_response
from forum_app.api_packs.user_api.user_details import get_details_user


def get_forum_users_list(data):
    code = 0
    posts_list = []

    forum_sh_name = data.get('forum')[0]

    since = data.get('since', [0, ])[0]

    limit = data.get('limit', [0, ])[0]

    sort_by = data.get('sort', 'flat')

    is_desc = 0
    order_by = data.get('order', 'desc')
    if 'desc' in order_by:
        is_desc = 1

    sql_scheme = {
        'columns_names': ['short_name'],
        'columns_values': [forum_sh_name],
        'table': 'Forum'
    }
    sql_check = build_sql_select_all_query(sql_scheme)

    res = open_sql(sql_check)  # check if exists

    if not res:
        code = 2
    else:
        sql_scheme = {
            'columns_names': ['forum'],
            'columns_values': [res['short_name']],
            'table': 'Post'
        }

        larger = {'id': since}

        group = 'user'

        sql = build_sql_select_all_query(sql_scheme, is_desc, limit, larger, group)
        posts_list = open_sql_all(sql)

    resp_list = []
    final_resp = make_response(code=code)

    if code == 0 and posts_list:
        for res in posts_list:
            resp_values = get_details_user(data={"user": [res['user'], ]})
            resp_list.append(resp_values['response'])

        final_resp = {'code': code, 'response': resp_list}
    return final_resp
