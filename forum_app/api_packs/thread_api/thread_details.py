__author__ = 'kic'

import flask
from forum_app.api_packs.db_queries.queries import exec_sql, open_sql, build_sql_insert_query, \
    build_sql_select_all_query
from forum_app.api_packs.make_response.make_response import make_response
from forum_app.api_packs.forum_api.forum_details import get_details_forum
from forum_app.api_packs.user_api.user_details import get_details_user


def get_details_thread(data):
    code = 0

    thread_id = data.get('thread', None)[0]

    related = data.get('related', None)

    sql_scheme = {
        'columns_names': ['id'],
        'columns_values': [thread_id],
        'table': 'Thread'
    }

    sql_check = build_sql_select_all_query(sql_scheme)

    res = open_sql(sql_check)  # check if exists

    if not res:
        code = 2
    else:
        user_data = {'user_id': [res['user'], ], 'user': [None, ]}
        user_resp = get_details_user(user_data, by_id=True)
        res['user'] = user_resp['response']['email']

        if related:
            forum_data = {'forum': [res['forum']], }
            forum_resp = get_details_forum(forum_data)
            res['forum'] = forum_resp['response']

            res['user'] = user_resp['response']

        keys = ['id', 'date', 'dislikes', 'forum', 'isClosed', 'isDeleted', 'likes', 'message', 'points', 'posts',
                'slug', 'title', 'user']
        values = [res['id'], str(res['date']), res['dislikes'], res['forum'], bool(res['isClosed']),
                  bool(res['isDeleted']), res['likes'], res['message'], res['points'], res['posts'], res['slug'],
                  res['title'], res['user']]

    resp_dict = make_response(keys, values, code)

    return resp_dict