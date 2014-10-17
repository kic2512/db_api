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
    post_id = data.get('post', None)[0]

    related = data.get('related', None)

    sql_scheme = {
        'columns_names': ['id'],
        'columns_values': [post_id],
        'table': 'Post'
    }

    sql_check = build_sql_select_all_query(sql_scheme)

    res = open_sql(sql_check)  # check if exists

    if not res:
        code = 2
    else:
        if related:

            forum_data = {'forum': [res['forum']], }
            forum_resp = get_details_forum(forum_data)
            res['forum'] = forum_resp['response']

            user_data = {'user': [res['user'], ]}
            user_resp = get_details_user(user_data)
            res['user'] = user_resp['response']

            thread_data = {'thread': [res['thread'], ]}
            thread_resp = get_details_thread(thread_data)
            res['thread'] = thread_resp['response']

        resp_keys = ['date', 'forum', 'id', 'isApproved', 'isDeleted', 'isEdited', 'isHighlighted', 'isSpam', 'message',
                     'parent', 'thread', 'user']

        resp_values = [str(res['date']), res['forum'], res['id'], bool(res['isApproved']), bool(res['isDeleted']),
                       bool(res['isEdited']), bool(res['isHighlighted']), bool(res['isSpam']), res['message'],
                       res['parent'], res['thread'], res['user']]

    resp_dict = make_response(resp_keys, resp_values, code)

    return resp_dict

