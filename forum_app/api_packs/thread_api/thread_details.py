__author__ = 'kic'

import flask
from forum_app.api_packs.db_queries.queries import exec_sql, open_sql, build_sql_insert_query, \
    build_sql_select_all_query, open_sql_all
from forum_app.api_packs.make_response.make_response import make_response
from forum_app.api_packs.forum_api.forum_details import get_details_forum
from forum_app.api_packs.user_api.user_details import get_details_user


def get_details_thread(data):
    code = 0
    keys = []
    values = []
    if not data:
        resp_dict = make_response(keys, values, code=4)
        return flask.jsonify(resp_dict)

    thread_id = data.get('thread', None)[0]
    related = data.get('related', None)
    if related and 'thread' in related:
        code = 3

    sql_scheme = {
        'columns_names': ['id'],
        'columns_values': [thread_id],
        'table': 'Thread'
    }

    is_closing = data.get('is_closing', [1, ])[0]
    cursor = data.get('cursor', [1, ])[0]

    sql_check = build_sql_select_all_query(sql_scheme)

    if is_closing == 1 and cursor == 1:
        res = open_sql(sql_check)  # check if exists
    else:
        res = open_sql(sql_check, first=False, is_closing=False, cursor=cursor)['result']

    if not res:
        code = 2
    else:
        if related and cursor == 1:
            forum_data = {'forum': [res['forum']], }
            forum_resp = get_details_forum(forum_data)
            res['forum'] = forum_resp['response']

            user_data = {'user': [res['user'], ]}
            user_resp = get_details_user(user_data)
            res['user'] = user_resp['response']

        keys = ['id', 'date', 'dislikes', 'forum', 'isClosed', 'isDeleted', 'likes', 'message', 'points', 'posts',
                'slug', 'title', 'user']

        #if res['isDeleted']:
        #    res['posts'] = 0
        values = [res['id'], str(res['date']), res['dislikes'], res['forum'], bool(res['isClosed']),
                  bool(res['isDeleted']), res['likes'], res['message'], res['points'], res['posts'], res['slug'],
                  res['title'], res['user']]

    resp_dict = make_response(keys, values, code)

    return resp_dict