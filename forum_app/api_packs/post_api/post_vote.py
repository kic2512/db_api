__author__ = 'kic'

import flask
from forum_app.api_packs.db_queries.queries import open_sql, exec_sql, build_sql_select_all_query, \
    build_sql_update_query
from forum_app.api_packs.make_response.make_response import make_response


def determinate_vote_column(val):
    res = 'likes'
    if val == -1:
        res = 'dislikes'
    return res


def vote_post(data):
    code = 0

    post_id = data['post']
    vote = data['vote']

    vote_column = determinate_vote_column(vote)

    sql_scheme = {
        'columns_names': ['id'],
        'columns_values': [post_id],
        'table': 'Post'
    }

    sql_check = build_sql_select_all_query(sql_scheme)
    res = open_sql(sql_check)

    if res:

        sql1 = "update Post set %s = %s+1 where id=%s" % (vote_column, vote_column, post_id)
        exec_sql(sql1)
        sql2 = "update Post set points=likes-dislikes  where id=%s" % post_id
        exec_sql(sql2)
        res = open_sql(sql_check)  # refresh

    else:
        code = 1

    resp_keys = ['date', 'forum', 'id', 'isApproved', 'isDeleted', 'isEdited', 'isHighlighted', 'isSpam', 'message',
                 'parent', 'thread', 'user']
    resp_values = [str(res['date']), res['forum'], res['id'], bool(res['isApproved']), bool(res['isDeleted']),
                   bool(res['isEdited']), bool(res['isHighlighted']), bool(res['isSpam']), res['message'],
                   res['parent'], res['thread'], res['user']]

    resp_dict = make_response(resp_keys, resp_values, code)
    return flask.jsonify(resp_dict)