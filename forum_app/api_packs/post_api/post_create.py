__author__ = 'kic'

import flask
from forum_app.api_packs.db_queries.queries import exec_sql, open_sql
from forum_app.api_packs.make_response.make_response import make_response
from forum_app.api_packs.db_queries.queries import build_sql_insert_query, build_sql_select_all_query, \
    build_sql_update_query

from forum_app.api_packs.user_api.user_details import get_details_user
from forum_app.api_packs.post_api.post_details import get_details_post


def create_post(data):
    code = 0

    if not data:
        resp_dict = make_response([], [], 3)
        return flask.jsonify(resp_dict)

    date = data['date']
    thread = data['thread']
    message = data['message']
    forum = data['forum']

    email = data['user']

    #usr_details = get_details_user({'user': [user, ]})['response']

    #usr_id = usr_details['id']

    parent = data.get('parent', None)

    isapproved = data.get('isApproved', 'False')

    if 'isHighlighted' in data:
        ishighlighted = data['isHighlighted']
    else:
        ishighlighted = 'False'

    if 'isEdited' in data:
        isedited = data['isEdited']
    else:
        isedited = 'False'

    if 'isSpam' in data:
        isspam = data['isSpam']
    else:
        isspam = 'False'

    if 'isDeleted' in data:
        isdeleted = data['isDeleted']
    else:
        isdeleted = 'False'

    res = False
    if not res:
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

        sql_scheme = {
            'columns_names': ['date', 'thread', 'message', 'user', 'forum', 'parent',
                              'isapproved', 'ishighlighted', 'isedited', 'isspam',
                              'isdeleted', 'mp'],
            'columns_values': [date, thread, message, email, forum, parent,
                               int(isapproved), int(ishighlighted), int(isedited), int(isspam),
                               int(isdeleted), mp],
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
            sql_check = build_sql_select_all_query(sql_scheme, what=' id ')
            res = open_sql(sql_check)
        else:
            code = 4

    post_data = {'post': [int(res['id']), ]}

    #post_resp = get_details_post(post_data)   add this after load

    #resp_dict = post_resp['response']         add this after load

    return flask.jsonify(post_data)