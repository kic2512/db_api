__author__ = 'kic'

import flask
from forum_app.api_packs.db_queries.queries import exec_sql, open_sql, build_sql_insert_query, \
    build_sql_select_all_query
from forum_app.api_packs.make_response.make_response import make_response
from forum_app.api_packs.forum_api.forum_details import get_details_forum
from forum_app.api_packs.user_api.user_details import get_details_user
from forum_app.api_packs.thread_api.thread_details import get_details_thread


def get_details_post(data):
    code = 0
    resp_keys = []
    resp_values = []

    post_id = data.get('post', None)[0]
    related = data.get('related', None)

    attributes = ' * '
    only_mp = data.get('only_mp', None)
    if only_mp:
        attributes = ' mp '

    sql_scheme = {
        'columns_names': ['id'],
        'columns_values': [post_id],
        'table': 'Post'
    }
    sql_check = build_sql_select_all_query(sql_scheme, what=attributes)

    is_closing = data.get('is_closing', [1, ])[0]
    cursor = data.get('cursor', [1, ])[0]

    if is_closing == 1 and cursor == 1:
        res = open_sql(sql_check)  # check if exists
    else:
        res = open_sql(sql_check, first=False, is_closing=False, cursor=cursor)['result']

    if not res:
        code = 1
    else:
        if related and is_closing == 1:
            forum_data = {'forum': [res['forum']], }
            forum_resp = get_details_forum(forum_data)
            res['forum'] = forum_resp['response']

            user_data = {'user': [res['user'], ]}
            user_resp = get_details_user(user_data)
            res['user'] = user_resp['response']

            thread_data = {'thread': [res['thread'], ]}
            thread_resp = get_details_thread(thread_data)
            res['thread'] = thread_resp['response']

        if not only_mp:
            resp_keys = ['date', 'forum', 'id', 'isApproved', 'isDeleted', 'isEdited', 'isHighlighted', 'isSpam',
                         'message', 'parent', 'thread', 'user', 'likes', 'dislikes', 'points']

            resp_values = [str(res['date']), res['forum'], int(post_id), bool(res['isApproved']),
                           bool(res['isDeleted']), bool(res['isEdited']), bool(res['isHighlighted']),
                           bool(res['isSpam']), res['message'], res['parent'], res['thread'], res['user'], res['likes'],
                           res['dislikes'], res['points']]
        else:
            resp_keys = ['mp']
            resp_values = [res['mp']]

    resp_dict = make_response(resp_keys, resp_values, code)

    return resp_dict