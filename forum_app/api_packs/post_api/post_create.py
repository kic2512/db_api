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
    date = data['date']
    thread = data['thread']
    message = data['message']
    forum = data['forum']

    user = data['user']

    usr_details = get_details_user({'user': [user, ]})['response']

    usr_id = usr_details['id']

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

    # sql_check = "select * from Post where user = '%s' and date= '%s' " % (user, date)

    sql_scheme = {
        'columns_names': ['user', 'date', 'message'],
        'columns_values': [usr_id, date, message],
        'table': 'Post'
    }
    sql_check = build_sql_select_all_query(sql_scheme)
    #res = open_sql(sql_check)  # check if exists
    res = False
    if not res:

        sql_scheme = {
            'columns_names': ['date', 'thread', 'message', 'user', 'forum', 'parent',
                              'isapproved', 'ishighlighted', 'isedited', 'isspam',
                              'isdeleted'],
            'columns_values': [date, thread, message, usr_id, forum, parent,
                               int(isapproved), int(ishighlighted), int(isedited), int(isspam),
                               int(isdeleted)],
            'table': 'Post'
        }
        sql_post = build_sql_insert_query(sql_scheme)
        sql_thread = " update Thread  set posts = posts+1 where id = %s ;" % thread

        exec_message1 = exec_sql([sql_post, sql_thread], multi=True)

        if exec_message1 == 0:
            res = open_sql(sql_check)
        else:
            code = 4
    # return str(res)
    post_data = {'post': [int(res['id']), ]}

    post_resp = get_details_post(post_data)

    #resp_dict = post_resp['response']

    return flask.jsonify(post_resp)