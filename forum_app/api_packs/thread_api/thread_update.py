__author__ = 'kic'

import flask
from forum_app.api_packs.db_queries.queries import exec_sql, open_sql, build_sql_select_all_query, \
    build_sql_update_query
from forum_app.api_packs.make_response.make_response import make_response


def update_thread(data):
    code = 0
    keys = []
    values = []

    thread_id = data['thread']
    message = data['message']
    slug = data['slug']

    sql_scheme = {
        'columns_names': ['id'],
        'columns_values': [thread_id],
        'table': 'Thread'
    }

    sql_check = build_sql_select_all_query(sql_scheme)
    res = open_sql(sql_check)

    if res:
        sql_scheme = {
            'columns_names': ['message', 'slug'],
            'columns_values': [message, slug],
            'condition': {'id': thread_id},
            'table': 'Thread'
        }
        sql_update = build_sql_update_query(sql_scheme)
        exec_sql(sql_update)

        keys = ['id', 'date', 'dislikes', 'forum', 'isClosed', 'isDeleted', 'likes', 'message', 'points', 'posts',
                'slug', 'title', 'user']

        values = [res['id'], str(res['date']), res['dislikes'], res['forum'], bool(res['isClosed']),
                  bool(res['isDeleted']), res['likes'], res['message'], res['points'], res['posts'], res['slug'],
                  res['title'], res['user']]
    else:
        code = 1

    resp_dict = make_response(keys=keys, values=values, code=code)
    return flask.jsonify(resp_dict)


