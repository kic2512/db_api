from forum_app.api_packs.user_api.user_details import get_details_user

__author__ = 'kic'

import flask
from forum_app.api_packs.db_queries.queries import exec_sql, open_sql, open_sql_all, build_sql_insert_query, \
    build_sql_select_all_query
from forum_app.api_packs.make_response.make_response import make_response


def get_thread_list(data):
    code = 0
    posts_list = []

    user_email = data.get('user', [0, ])[0]
    forum_sh_name = data.get('forum', [0, ])[0]

    req_field = {'name': 'short_name', 'val': forum_sh_name, 'table': 'Forum', 'related': 'forum'}
    if user_email:
        req_field = {'name': 'email', 'val': user_email, 'table': 'User', 'related': 'user'}

    since = data.get('since', [0, ])[0]

    limit = data.get('limit', [0, ])[0]

    sort_by = data.get('sort', 'flat')

    is_desc = 0
    order_by = data.get('order', 'desc')
    if 'desc' in order_by:
        is_desc = 1

    sql_scheme = {
        'columns_names': [req_field['name']],
        'columns_values': [req_field['val']],
        'table': req_field['table']
    }
    sql_check = build_sql_select_all_query(sql_scheme)

    res = open_sql(sql_check)  # check if exists

    if not res:
        code = 2
    else:
        sql_scheme = {
            'columns_names': [req_field['related']],
            'columns_values': [req_field['val']],
            'table': 'Thread'
        }
        if since != 0:
            larger = {'date': since}
            sql = build_sql_select_all_query(sql_scheme, is_desc, limit, larger)
        else:
            sql = build_sql_select_all_query(sql_scheme, is_desc, limit)

        posts_list = open_sql_all(sql)

    keys = ['id', 'date', 'forum', 'isClosed', 'isDeleted', 'message', 'slug', 'title', 'user', 'posts']

    resp_dict = []
    final_resp = make_response(code=code)

    if code == 0 and posts_list:
        for res in posts_list:
            values = [res['id'], str(res['date']), res['forum'], bool(res['isClosed']), bool(res['isDeleted']),
                      res['message'], res['slug'], res['title'], res['user'], res['posts']]

            resp_dict.append(make_response(keys, values, code)['response'])
        final_resp = {'code': code, 'response': resp_dict}

    return final_resp
