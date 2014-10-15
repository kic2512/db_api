__author__ = 'kic'

import flask
from forum_app.api_packs.db_queries.queries import exec_sql, open_sql, build_sql_select_all_query, \
    build_sql_update_query
from forum_app.api_packs.make_response.make_response import make_response


def update_post(data):
    code = 0
    keys = []
    values = []

    post_id = data['post']
    message = data['message']

    sql_scheme = {
        'columns_names': ['id'],
        'columns_values': [post_id],
        'table': 'Post'
    }

    sql_check = build_sql_select_all_query(sql_scheme)
    res = open_sql(sql_check)

    if res:
        sql_scheme = {
            'columns_names': ['message'],
            'columns_values': [message],
            'condition': {'id': post_id},
            'table': 'Post'
        }
        exec_sql(build_sql_update_query(sql_scheme))
        keys = ['date', 'dislikes', 'forum', 'id', 'isApproved', 'isDeleted', 'isEdited', 'isHighlighted', 'isSpam',
                'likes', 'message', 'parent', 'points', 'thread', 'user']

        values = [res['date'], res['dislikes'], res['forum'], res['id'], res['isApproved'], res['isDeleted'],
                  res['isEdited'], res['isHighlighted'], res['isSpam'], res['likes'], message, res['parent'],
                  res['points'], res['thread'], res['user']]
        values = [str(x) for x in values]
    else:
        code = 1

    resp_dict = make_response(keys=keys, values=values, code=code)
    return flask.jsonify(resp_dict)

