__author__ = 'kic'

import flask
from forum_app.api_packs.db_queries.queries import exec_sql, open_sql
from forum_app.api_packs.make_response.make_response import make_response
from forum_app.api_packs.db_queries.queries import build_sql_insert_query, build_sql_select_all_query, \
    build_sql_update_query


def create_post(data):
    code = 0
    date = data['date']
    thread = data['thread']
    message = data['message']
    user = data['user']
    forum = data['forum']

    if 'parent' in data:
        parent = data['parent']
    else:
        parent = None

    if 'isApproved' in data:
        isapproved = data['isApproved']
    else:
        isapproved = 'False'

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
        'columns_names': ['user', 'date'],
        'columns_values': [user, date],
        'table': 'Post'
    }

    sql_check = build_sql_select_all_query(sql_scheme)
    res = open_sql(sql_check)  # check if exists
    if not res:

        sql_scheme = {
            'columns_names': ['date', 'thread', 'message', 'user', 'forum', 'parent',
                              'isapproved', 'ishighlighted', 'isedited', 'isspam',
                              'isdeleted'],
            'columns_values': [date, thread, message, user, forum, parent,
                               int(isapproved), int(ishighlighted), int(isedited), int(isspam),
                               int(isdeleted)],
            'table': 'Post'
        }
        sql = build_sql_insert_query(sql_scheme)
        exec_message1 = exec_sql(sql)

        sql = " update Thread  set posts = posts+1 where id = %s ;" % thread

        exec_message2 = exec_sql(sql)

        if exec_message1 == exec_message2 == 0:
            res = open_sql(sql_check)
        else:
            code = 4
    # return str(res)

    resp_keys = ['date', 'forum', 'id', 'isApproved', 'isDeleted', 'isEdited', 'isHighlighted', 'isSpam', 'message',
                 'parent', 'thread', 'user']
    resp_values = [res['date'], res['forum'], res['id'], bool(res['isApproved']), bool(res['isDeleted']),
                   bool(res['isEdited']), bool(res['isHighlighted']), bool(res['isSpam']), res['message'],
                   res['parent'], res['thread'], res['user']]

    resp_dict = make_response(resp_keys, resp_values, code)

    return flask.jsonify(resp_dict)