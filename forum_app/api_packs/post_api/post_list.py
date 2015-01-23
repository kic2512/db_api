from forum_app.api_packs.user_api.user_details import get_details_user

__author__ = 'kic'

import flask
from forum_app.api_packs.db_queries.queries import exec_sql, open_sql, open_sql_all, build_sql_insert_query, \
    build_sql_select_all_query
from forum_app.api_packs.make_response.make_response import make_response


def get_post_list(data):
    code = 0
    posts_list = []

    thread_id = data.get('thread', [0, ])[0]
    forum_sh_name = data.get('forum', [0, ])[0]

    req_field = {'name': 'short_name', 'val': forum_sh_name, 'table': 'Forum', 'related': 'forum'}
    if thread_id:
        req_field = {'name': 'id', 'val': thread_id, 'table': 'Thread', 'related': 'thread'}

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

    res_dict = open_sql_all(sql_check, first=True, is_closing=False)  # check if exists
    res = res_dict['result'][0]
    if res == -1 or not res:
        return make_response([], [], code=4)

    db = res_dict['db']
    crs = res_dict['cursor']

    if not res:
        code = 2
    else:
        sql_scheme = {
            'columns_names': [req_field['related']],
            'columns_values': [req_field['val']],
            'table': 'Post'
        }
        if since != 0:
            larger = {'date': since}
            sql = build_sql_select_all_query(sql_scheme, is_desc, limit, larger)
        else:
            sql = build_sql_select_all_query(sql_scheme, is_desc, limit)

        posts_list = open_sql_all(sql, first=False, cursor=crs, is_closing=False)['result']
        if posts_list == -1 or not posts_list:
            return make_response([], [], code=4)

    resp_keys = ['date', 'forum', 'id', 'isApproved', 'isDeleted', 'isEdited', 'isHighlighted', 'isSpam', 'message',
                 'parent', 'thread', 'user', 'likes', 'dislikes', 'points']

    resp_dict = []
    final_resp = make_response(code=code)

    if code == 0 and posts_list:
        for res in posts_list:
            resp_values = [str(res['date']), res['forum'], res['id'], bool(res['isApproved']), bool(res['isDeleted']),
                           bool(res['isEdited']), bool(res['isHighlighted']), bool(res['isSpam']), res['message'],
                           res['parent'], res['thread'], res['user'], res['likes'], res['dislikes'], res['points']]
            resp_dict.append(make_response(resp_keys, resp_values, code)['response'])
        final_resp = {'code': code, 'response': resp_dict}

    db.close()
    return final_resp