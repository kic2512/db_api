from forum_app.api_packs.post_api.post_details import get_details_post
from forum_app.api_packs.user_api.user_details import get_details_user

__author__ = 'kic'

import flask
from forum_app.api_packs.db_queries.queries import exec_sql, open_sql, open_sql_all, build_sql_insert_query, \
    build_sql_select_all_query
from forum_app.api_packs.make_response.make_response import make_response


def get_thread_list_posts(data):
    code = 0
    posts_list = []

    thread_id = data.get('thread')[0]

    since = data.get('since', [0, ])[0]
    larger = {'date': since}

    limit = data.get('limit', [0, ])[0]

    sort_by = data.get('sort', 'flat')

    is_desc = 0
    order_by = data.get('order', ['asc', ])
    if 'desc' in order_by:
        is_desc = 1

    sql_scheme = {
        'columns_names': ['id'],
        'columns_values': [thread_id],
        'table': 'Thread'
    }
    sql_check = build_sql_select_all_query(sql_scheme, what=' id ')

    res_dict = open_sql_all(sql_check, first=True, is_closing=False)  # check if exists

    res = res_dict['result'][0]
    db = res_dict['db']
    crs = res_dict['cursor']

    if not res:
        code = 2
    else:
        sql_scheme = {
            'columns_names': ['thread'],
            'columns_values': [thread_id],
            'table': 'Post'
        }
        if since != 0:
            sql = build_sql_select_all_query(sql_scheme, is_desc=is_desc, limit=limit, larger=larger, what=' id,user ')
        else:
            sql = build_sql_select_all_query(sql_scheme, is_desc=is_desc, limit=limit, what=' id,user ')

        posts_list = open_sql_all(sql, first=False, cursor=crs, is_closing=False)['result']

    final_resp = []

    if code == 0 and posts_list:
        for res in posts_list:
            post_data = {'post': [res['id'], ], 'is_closing': [False, ], 'cursor': [crs, ]}
            post_resp = get_details_post(post_data)['response']
            final_resp.append(post_resp)

    out_dict = {'code': code, 'response': final_resp}

    db.close()
    return out_dict