__author__ = 'kic'

import flask
from forum_app.api_packs.db_queries.queries import exec_sql, open_sql, build_sql_select_all_query, \
    build_sql_update_query
from forum_app.api_packs.make_response.make_response import make_response


def remove_thread(data):
    code = 0
    thread = data['thread']

    sql_scheme = {
        'columns_names': ['id'],
        'columns_values': [thread],
        'table': 'Thread'
    }

    sql_check = build_sql_select_all_query(sql_scheme)
    res = open_sql(sql_check)
    if res:
        sql_scheme_posts_count = {
            'columns_names': ['thread'],
            'columns_values': [thread],
            'table': 'Post'
        }

        sql_posts_count = build_sql_select_all_query(sql_scheme_posts_count)
        res_posts = open_sql(sql_posts_count)

        posts_count = 0
        if res_posts:
            posts_count = len([res_posts])

        """
        TODO
        sql_scheme_thread_up = {
            'columns_names': ['isDeleted', 'posts'],
            'columns_values': [1, 'posts-'+str(posts_count)],
            'condition': {'id': thread},
            'table': 'Thread'
        }
        """

        sql_thread_up = 'update Thread set  posts=0 , isDeleted=1  where  id = %s' % thread
        exec_sql(sql_thread_up)

        sql_scheme_post_rm = {
            'columns_names': ['isDeleted'],
            'columns_values': [1],
            'condition': {'thread': thread},
            'table': 'Post'
        }
        sql_post_rm = build_sql_update_query(sql_scheme_post_rm)
        exec_sql(sql_post_rm)

        sql_check = build_sql_select_all_query(sql_scheme)
        res = open_sql(sql_check)

    if not res:
        code = 1

    keys = ['thread']
    values = [thread]

    resp_dict = make_response(keys, values, code)
    return flask.jsonify(resp_dict)

