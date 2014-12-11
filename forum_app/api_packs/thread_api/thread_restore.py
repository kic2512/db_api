__author__ = 'kic'

import flask
from forum_app.api_packs.db_queries.queries import exec_sql, open_sql, build_sql_select_all_query, \
    build_sql_update_query, open_sql_all
from forum_app.api_packs.make_response.make_response import make_response


def restore_thread(data):
    code = 0
    thread = data['thread']

    sql_scheme = {
        'columns_names': ['id', 'isDeleted'],
        'columns_values': [thread, 1],
        'table': 'Thread'
    }

    sql_check = build_sql_select_all_query(sql_scheme)
    res = open_sql(sql_check)
    if res:

        sql_scheme_post_cont = {
            'columns_names': ['thread'],
            'columns_values': [thread],
            'table': 'Post'
        }
        sql_post_count = build_sql_select_all_query(sql_scheme_post_cont, what='COUNT(*)')
        res_count = open_sql(sql_post_count)

        posts_count = 0

        if res_count:
            posts_count = res_count['COUNT(*)']
        """
        TODO
        sql_scheme_thread_up = {
            'columns_names': ['isDeleted', 'posts'],
            'columns_values': [0, 'posts+'+str(posts_count)],
            'condition': {'id': thread},
            'table': 'Thread'
        }"""

        sql1 = 'update Thread set  posts=%s , isDeleted=0  where  id = %s' % (posts_count, thread)
        exec_sql(sql1)

        sql_scheme_post_up = {
            'columns_names': ['isDeleted'],
            'columns_values': [0],
            'condition': {'thread': thread},
            'table': 'Post'
        }
        sql2 = build_sql_update_query(sql_scheme_post_up)
        exec_sql(sql2)

        #if (exec_message1 == exec_message2) != 0:
        #    code = 4
    if not res:
        code = 1

    keys = ['thread']
    values = [thread]

    resp_dict = make_response(keys, values, code)
    return flask.jsonify(resp_dict)