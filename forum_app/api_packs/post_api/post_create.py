__author__ = 'kic'

import flask
from forum_app.api_packs.db_queries.queries import exec_sql, open_sql
from forum_app.api_packs.make_response.make_response import make_response
from forum_app.api_packs.db_queries.queries import build_sql_query


def create_post(data):
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

    sql_check = "select * from Post where user = '%s' and date= '%s' " % (user, date)
    res = open_sql(sql_check)  # check if exists

    if not res:
        sql_scheme = {
            'columns_names': ['date', 'thread', 'message', 'user', 'forum', 'parent',
                              'isapproved', 'ishighlighted', 'isedited', 'isspam',
                              'isdeleted'],
            'columns_values': [str(date), str(thread), str(message), str(user), str(forum), str(parent),
                               str(isapproved),
                               str(ishighlighted), str(isedited), str(isspam), str(isdeleted)],
            'table': 'Post',
            'type': 'insert'}
        return 'intro'
        sql = build_sql_query(sql_scheme)
        res = exec_sql(sql)

        if res == 0:
            res = open_sql(sql_check)
        else:
            TODO = None
    # return str(res)

    resp_keys = ['date', 'forum', 'id', 'isApproved', 'isDeleted', 'isEdited', 'isHighlighted', 'isSpam', 'message',
                 'parent', 'thread', 'user']
    resp_values = [res['date'], res['forum'], res['id'], bool(res['isApproved']), bool(res['isDeleted']),
                   bool(res['isEdited']), bool(res['isHighlighted']), bool(res['isSpam']), res['message'],
                   res['parent'], res['thread'], res['user']]

    resp_dict = make_response(keys=resp_keys, values=resp_values)

    return flask.jsonify(resp_dict)

