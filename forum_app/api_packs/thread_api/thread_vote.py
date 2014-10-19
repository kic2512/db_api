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


def vote_thread(data):
    code = 0

    thread_id = data['thread']
    vote = data['vote']

    vote_column = determinate_vote_column(vote)

    sql_scheme = {
        'columns_names': ['id'],
        'columns_values': [thread_id],
        'table': 'Thread'
    }

    sql_check = build_sql_select_all_query(sql_scheme)
    res = open_sql(sql_check)

    if res:

        sql1 = "update Thread set %s = %s+1 where id=%s" % (vote_column, vote_column, thread_id)
        sql2 = "update Thread set points=likes-dislikes  where id=%s" % thread_id

        exec_sql("START TRANSACTION;")
        exec_sql(sql1)
        exec_sql(sql2)
        exec_sql("COMMIT;")

        res = open_sql(sql_check)  # refresh

    else:
        code = 1

    keys = ['id', 'date', 'forum', 'isClosed', 'isDeleted', 'message', 'slug', 'title', 'user', 'likes', 'dislikes',
            'points']
    values = [res['id'], str(res['date']), res['forum'], bool(res['isClosed']), bool(res['isDeleted']), res['message'],
              res['slug'], res['title'], res['user'], res['likes'], res['dislikes'], res['points']]

    resp_dict = make_response(keys, values, code)
    return flask.jsonify(resp_dict)