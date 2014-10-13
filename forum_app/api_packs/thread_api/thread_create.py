__author__ = 'kic'
import flask
from forum_app.api_packs.db_queries.queries import exec_sql, open_sql
from forum_app.api_packs.make_response.make_response import make_response


def create_thread(data):
    forum = data['forum']
    title = data['title']
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

        sql = "insert into Thread (forum, title, isClosed, user, date, message, slug, isDeleted)" \
              " values('%s','%s','%d','%s','%s','%s','%s','%d')" % (
                  forum, title.decode('utf-8'), int(isclosed), user, date, message, slug, int(isdeleted))

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
