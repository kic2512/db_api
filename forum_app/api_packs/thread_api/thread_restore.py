__author__ = 'kic'

import flask
from forum_app.api_packs.db_queries.queries import exec_sql, open_sql, build_sql_select_all_query, \
    build_sql_update_query
from forum_app.api_packs.make_response.make_response import make_response


def restore_thread(data):
    code = 0
    thread = data['thread']

    sql_scheme = {
        'columns_names': ['id'],
        'columns_values': [thread],
        'table': 'Thread'
    }

    sql_check = build_sql_select_all_query(sql_scheme)
    res = open_sql(sql_check)
    if 'isDeleted' in res and res['isDeleted']:
        sql_scheme = {
            'columns_names': ['isDeleted'],
            'columns_values': [0],
            'condition': {'id': thread},
            'table': 'Thread'
        }

        sql_scheme2 = {
            'columns_names': ['isDeleted'],
            'columns_values': [0],
            'condition': {'thread': thread},
            'table': 'Post'
        }

        exec_sql("START TRANSACTION;")
        exec_sql(build_sql_update_query(sql_scheme))
        exec_sql(build_sql_update_query(sql_scheme2))
        exec_sql("COMMIT;")

        #if (exec_message1 == exec_message2) != 0:
        #    code = 4
    if not res:
        code = 1

    keys = ['thread']
    values = [thread]

    resp_dict = make_response(keys, values, code)
    return flask.jsonify(resp_dict)