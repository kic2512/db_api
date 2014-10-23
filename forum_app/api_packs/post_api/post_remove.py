__author__ = 'kic'

import flask
from forum_app.api_packs.db_queries.queries import exec_sql, open_sql, build_sql_select_all_query, \
    build_sql_update_query
from forum_app.api_packs.make_response.make_response import make_response


def remove_post(data):
    code = 0
    post = data['post']

    sql_scheme = {
        'columns_names': ['id'],
        'columns_values': [post],
        'table': 'Post'
    }

    sql_check = build_sql_select_all_query(sql_scheme)
    res = open_sql(sql_check)

    if ('isDeleted' in res) and (not res['isDeleted']):
        sql_scheme = {
            'columns_names': ['isDeleted'],
            'columns_values': [1],
            'condition': {'id': post},
            'table': 'Post'
        }

        sql_update = build_sql_update_query(sql_scheme)
        sql = " update Thread set posts=posts-1 where id= %s " % res['thread']
        #return sql
        exec_message = exec_sql([sql_update, sql], multi=True)

        if exec_message != 0:
            code = 4

    if not res:
        code = 1

    keys = ['post']
    values = [post]

    resp_dict = make_response(keys, values, code)
    return flask.jsonify(resp_dict)
