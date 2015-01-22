__author__ = 'kic'

import flask
from forum_app.api_packs.db_queries.queries import exec_sql, open_sql, open_sql_all, build_sql_insert_query, \
    build_sql_select_all_query
from forum_app.api_packs.make_response.make_response import make_response


def get_user_list_posts(data):
    code = 0
    posts_list = []

    user_email = data.get('user')[0]

    since = data.get('since', [0, ])[0]

    limit = data.get('limit', [0, ])[0]

    sort_by = data.get('sort', 'flat')

    is_desc = 0
    order_by = data.get('order', 'desc')
    if 'desc' in order_by:
        is_desc = 1

    sql_scheme = {
        'columns_names': ['email'],
        'columns_values': [user_email],
        'table': 'User'
    }
    sql_check = build_sql_select_all_query(sql_scheme)

    res = open_sql(sql_check)  # check if exists

    if not res:
        code = 5
    else:
        sql_scheme = {
            'columns_names': ['user'],
            'columns_values': [user_email],
            'table': 'Post'
        }
        larger = -1
        if since != 0:
            larger = {'date': since}
            sql = build_sql_select_all_query(sql_scheme, is_desc, limit, larger)
        else:
            sql = build_sql_select_all_query(sql_scheme, is_desc, limit)

        posts_list = open_sql_all(sql)

    resp_keys = ['date', 'forum', 'id', 'isApproved', 'isDeleted', 'isEdited', 'isHighlighted', 'isSpam', 'message',
                 'parent', 'thread', 'user', 'likes', 'dislikes', 'points']

    resp_dict = []
    final_resp = make_response(code=code)

    if code == 0 and posts_list:
        for res in posts_list:

            resp_values = [str(res['date']), res['forum'], res['id'], bool(res['isApproved']), bool(res['isDeleted']),
                           bool(res['isEdited']), bool(res['isHighlighted']), bool(res['isSpam']), res['message'],
                           res['parent'], res['thread'], res['user'], res['likes'], res['dislikes'],
                           res['points']]
            resp_dict.append(make_response(resp_keys, resp_values, code)['response'])
        final_resp = {'code': code, 'response': resp_dict}

    return final_resp
