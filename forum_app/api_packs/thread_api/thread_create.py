__author__ = 'kic'
import flask
from forum_app.api_packs.db_queries.queries import exec_sql, open_sql, build_sql_query
from forum_app.api_packs.make_response.make_response import make_response


def create_thread(data):
    forum = data['forum']
    title = data['title'].encode('utf-8')
    isclosed = data['isClosed']
    user = data['user']
    date = data['date']
    message = data['message']
    slug = data['slug']

    if 'isDeleted' in data:
        isdeleted = data['isDeleted']
    else:
        isdeleted = 'False'

    sql_check = "select * from Thread where title = '%s' " % title

    res = open_sql(sql_check)  # check if exists

    if not res:
        sql_scheme = {
            'columns_names': ['forum', 'title', 'isClosed', 'user', 'date', 'message', 'slug', 'isDeleted'],
            'columns_values': [str(forum), str(title), str(isclosed), str(user), str(date), str(message),
                               str(slug), str(isdeleted)],
            'table': 'Thread',
            'type': 'insert'}

        sql = build_sql_query(sql_scheme)
        res = exec_sql(sql)

        if res == 0:
            res = open_sql(sql_check)
        else:
            TODO = None
    # return str(res)
    keys = ['id', 'date', 'forum', 'isClosed', 'isDeleted', 'message', 'slug', 'title', 'user']
    values = [res['id'], res['date'], res['forum'], bool(res['isClosed']), bool(res['isDeleted']), res['message'],
              res['slug'], res['title'], res['user']]

    resp_dict = make_response(keys=keys, values=values)

    return flask.jsonify(resp_dict)
