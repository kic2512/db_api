__author__ = 'kic'

import flask
from forum_app.api_packs.db_queries.queries import exec_sql, open_sql, build_sql_select_all_query, \
    build_sql_update_query
from forum_app.api_packs.make_response.make_response import make_response


def restore_post(data):
    code = 0
    post = data['post']

    sql_scheme = {
        'columns_names': ['id'],
        'columns_values': [post],
        'table': 'Post'
    }

    sql_check = build_sql_select_all_query(sql_scheme)
    res = open_sql(sql_check)
    if ('isDeleted' in res) and res['isDeleted']:
        sql_scheme = {
            'columns_names': ['isDeleted'],
            'columns_values': [0],
            'condition': {'id': post},
            'table': 'Post'
        }
        sql = " update Thread set posts=posts+1 where id= %s ;" % res['thread']

        exec_sql("START TRANSACTION;")
        exec_sql(build_sql_update_query(sql_scheme))
        exec_sql(sql)
        exec_sql("COMMIT;")

    if not res:
        code = 1

    keys = ['post']
    values = [post]

    resp_dict = make_response(keys=keys, values=values, code=code)
    return flask.jsonify(resp_dict)
