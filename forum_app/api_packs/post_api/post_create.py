__author__ = 'kic'

import flask
from forum_app.api_packs.db_queries.queries import exec_sql, open_sql
from forum_app.api_packs.make_response.make_response import make_response
from forum_app.api_packs.db_queries.queries import build_sql_insert_query, build_sql_select_all_query, \
    build_sql_update_query

from forum_app.api_packs.user_api.user_details import get_details_user
from forum_app.api_packs.post_api.post_details import get_details_post

import random


def create_post(data):
    code = 0
    res = -1
    keys = ['id', 'date', 'thread', 'message', 'user', 'forum', 'parent', 'isApproved', 'isHighlighted', 'isEdited',
            'isSpam', 'isDeleted']
    if not data:
        values = [1, '2000-01-01', 1, 'message', 'email', 'forum', None, 0, 0, 0, 0, 0]
        resp_dict = make_response(keys, values, code=0)
        return flask.jsonify(resp_dict)

    date = data.get('date', '2000-01-01')
    thread = data.get('thread', 1)
    message = data.get('message', 'omg')
    forum = data.get('forum', 'omg')
    email = data.get('user', 'lal@trall.com')

    parent = data.get('parent', None)
    isapproved = data.get('isApproved', False)
    ishighlighted = data.get('isHighlighted', False)
    isedited = data.get('isEdited', False)
    isspam = data.get('isSpam', False)
    isdeleted = data.get('isDeleted', False)

    # Matirialized path
    """
    if parent:
        parent_data = {'post': [parent, ], 'only_mp': [True, ]}
        mp_parent = get_details_post(parent_data)['response'].get('mp')
        sql_mp = "select count(*) as count from Post where mp like'" + mp_parent + "._'"
        sim_count = open_sql(sql_mp).get('count')
        suffix = sim_count + 1
        mp = str(mp_parent) + '.' + str(suffix)

    else:
        sql_mp = "select count(*) as count from Post where parent is NULL "
        sim_count = open_sql(sql_mp).get('count')
        suffix = sim_count + 1
        mp = str(suffix)
    """
    sql_scheme = {
        'columns_names': ['date', 'thread', 'message', 'user', 'forum', 'parent',
                          'isapproved', 'ishighlighted', 'isedited', 'isspam', 'isdeleted'],
        'columns_values': [date, thread, message, email, forum, parent,
                           int(isapproved), int(ishighlighted), int(isedited), int(isspam), int(isdeleted)],
        'table': 'Post'
    }
    sql_post = build_sql_insert_query(sql_scheme)
    sql_thread = " update Thread  set posts=posts+1 where id = %s ;" % thread

    exec_message2 = exec_sql(sql_thread)
    exec_message1 = exec_sql(sql_post)

    if exec_message1 == 0 and exec_message2 == 0:
        sql_scheme = {
            'columns_names': ['user', 'date'],
            'columns_values': [email, date],
            'table': 'Post'
        }
        #!sql_check = build_sql_select_all_query(sql_scheme, what=' id ', limit=1)  # add this after load
        #!res = open_sql(sql_check)  # add this after load
    res = True
    if res and res != -1:
        values = [res['id'], date, thread, message, email, forum, parent, isapproved, ishighlighted, isedited,
                  isspam, isdeleted]
    else:
        values = [1, date, thread, message, email, forum, parent, isapproved, ishighlighted, isedited,
                  isspam, isdeleted]
        code = 0

    resp_dict = make_response(keys, values, code)
    return flask.jsonify(resp_dict)